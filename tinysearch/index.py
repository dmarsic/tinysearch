"""Index represents a reverted index.

Reverted index is a structure enabling search. It contains documents,
and each document has been parsed / analyzed to generate a list of
tokens (terms).

Then the search operates on the indexed documents to find the best results
for a given query.

Example usage:

    docs = [...]  # List of strings
    i = Index(docs)
    print(i.docs)
"""
from typing import List

from tinysearch.document import Document


class Index:
    def __init__(self, docs: List[str]) -> None:
        self.docs = self.process_docs(docs)

    def __str__(self):
        return f"Index[docs={len(self.docs)}]"

    def __repr__(self):
        return self.__str__()

    def process_docs(self, docs: List[str]) -> List[Document]:
        processed = []
        for doc in docs:
            d = Document(doc)
            d.analyze()
            processed.append(d)
        return processed
