from typing import List

from tinysearch.document import Document


class Index:

    def __init__(self, docs: List[str]) -> None:
        self.docs = self.process_docs(docs)

    def process_docs(self, docs: List[str]) -> List[Document]:
        processed = []
        for doc in docs:
            d = Document(doc)
            d.analyze()
            processed.append(d)
        return processed

