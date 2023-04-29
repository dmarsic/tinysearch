"""Index represents a reverted index.

Reverted index is a structure enabling search. It contains documents,
and each document has been parsed / analyzed to generate a list of
tokens (terms).

Then the search operates on the indexed documents to find the best results
for a given query.

Example usage:

    docs = [...]  # List of strings
    i = Index()
    i.index_docs(docs)
    print(i.docs)
"""
from tinysearch.document import Document
from tinysearch.base.analyzer import Analyzer
from tinysearch.analyzer import SimpleEnglishAnalyzer


class Index:
    def __init__(self, analyzer: Analyzer = None, stopwords: set[str] = set()) -> None:
        self.analyzer = analyzer if analyzer is not None else SimpleEnglishAnalyzer()
        self.stopwords = stopwords
        self.docs = []

    def __str__(self):
        return f"Index[docs={len(self.docs)}, analyzer={self.analyzer.__class__}]"

    def __repr__(self):
        return self.__str__()

    def index_docs(self, docs: list[str]) -> list[Document]:
        processed = []
        for doc in docs:
            d = Document(doc, analyzer=self.analyzer, stopwords=self.stopwords)
            processed.append(d)
        self.docs = processed
        return processed
