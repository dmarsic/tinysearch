from dataclasses import dataclass
from math import log
from typing import List

from tinysearch.index import Index
from tinysearch.document import Document
from tinysearch.analyzer import Analyzer


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

    def __init__(self, docs: List[str], query: str) -> None:
        self.index = Index(docs)
        self.query = query
        self.results = Results()
        self.search()

    def search(self) -> Results:
        self.score_docs(self.query)

    def score_docs(self, query: str):
        for doc in self.index.docs:
            score = self.score_doc(doc, query)
            self.results.append(Result(doc, score))

    def score_doc(self, doc: Document, query: str) -> float:
        tfidf_sum = 0.0
        a = Analyzer()
        query_tokens = a.analyze(query)
        for t in query_tokens:
            tfidf_sum += self.calculate_tfidf(doc, t)
        return tfidf_sum

    def calculate_tfidf(self, doc: Document, query_token: str) -> float:
        tf = doc.tokens[query_token] / sum(doc.tokens.values())

        doc_count = len(self.index.docs)
        contains_word_count = 0
        for doc in self.index.docs:
            if query_token in doc.tokens:
                contains_word_count += 1
        if contains_word_count == 0:
            return 0.0

        idf = log(doc_count / contains_word_count)

        tfidf = tf * idf

        return tfidf
