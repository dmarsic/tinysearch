"""Search runs a query against the index and finds best matches.

Index is a collection of processed documents. When a user passes
a query, the documents are scored against the query to find the
best matches.

Search provides results (see Results class), which contains scores
for all documents. The higher score is the better. Scoring is done
by applying the TF-IDF algorithm.

Users of this class will typically be interested in matches, which
is a filtered list of all results where the score is larger than
0.0, indicating that the document contains one or more query terms.

Example usage:

    docs = [...]  # List of strings
    query = "city lights"
    s = Search(docs, query)

    print(s.results.count)
    # 4

    print(s.results.matches[0])
    # Result(doc=..., score=0.20)
"""

from collections import defaultdict
from dataclasses import dataclass
from math import log
from typing import List

from tinysearch.index import Index
from tinysearch.document import Document
from tinysearch.base.analyzer import Analyzer
from tinysearch.analyzer import SimpleEnglishAnalyzer


@dataclass
class Result:
    doc: Document
    score: float

    def __str__(self):
        return f"doc={self.doc} score={self.score}"

    def __repr__(self):
        return self.__str__()


class Results:
    def __init__(self):
        self.results = []
        self._matches = []

    def __str__(self):
        return str(self.results)

    def __repr__(self):
        return self.__str__()

    def append(self, result: Result) -> None:
        self.results.append(result)
        if result.score > 0.0:
            self._matches.append(result)

    @property
    def count(self) -> int:
        return len(self._matches)

    @property
    def matches(self) -> List[Result]:
        return sorted(self._matches, key=lambda r: r.score, reverse=True)


class Search:
    def __init__(self, docs: List[str], query: str, analyzer: Analyzer = None) -> None:
        if query is None:
            raise ValueError("Query must be text.")

        self.analyzer = analyzer if analyzer is not None else SimpleEnglishAnalyzer()

        self.query = query
        self.results = Results()
        self.index = Index(docs, analyzer=self.analyzer)
        self.search()

    def __str__(self):
        return f"Search[query='{self.query}', matches={self.results.count}]"

    def __repr__(self):
        return self.__str__()

    def search(self) -> Results:
        """Search builds a result set of matched documents.

        It takes the query and splits it into tokens, and then
        calculates TF-IDF score for each document for each query
        token. A final TF-IDF score is the sum of TF-IDF scores
        for each query token.
        """
        query_tokens = self.analyzer.analyze(self.query)

        # Store the number of documents each query token appears in.
        occurs = defaultdict(int)
        for doc in self.index.docs:
            for token in query_tokens:
                occurs[token] += int(token in doc.tokens)

        # Calculate TF-IDF for each document.
        for doc in self.index.docs:
            tfidf_sum = 0.0

            for token in query_tokens:
                if occurs[token] == 0:
                    continue

                tf = doc.tokens[token] / sum(doc.tokens.values())
                idf = log(len(self.index.docs) / occurs[token])

                tfidf_sum += tf * idf

            self.results.append(Result(doc, tfidf_sum))
