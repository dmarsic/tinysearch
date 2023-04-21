"""Document represents a document to be indexed and searched.

Example usage:

    t = "There was the distinct sound of the tavern door smashing open."
    d = Document(t)

    print(d.tokens)
    # Counter({'there': 1,
    #     'was': 1,
    #     'the': 2,
    #     'distinct': 1,
    #     'sound': 1,
    #     'of': 1,
    #     'tavern': 1,
    #     'door': 1,
    #     'smashing': 1,
    #     'open': 1})
"""
from collections import Counter

from tinysearch.base.analyzer import Analyzer
from tinysearch.analyzer import SimpleEnglishAnalyzer


class Document:
    """Document that can be indexed and searched.

    Document is instantiated with the text value of a document.
    It can be parsed or analyzed, which produces a tokenized
    list (also called terms).
    """

    def __init__(self, original: str, analyzer: Analyzer = None):
        if original is None:
            raise ValueError(f"Document needs to be text.")

        self.analyzer = analyzer if analyzer is not None else SimpleEnglishAnalyzer()

        self.original = original
        self.tokens = self.analyze()

    def __str__(self):
        return f"Document['{self.original}']"

    def __repr__(self):
        return self.__str__()

    def analyze(self) -> Counter:
        """Parses the original text into a list of tokens."""
        tokens = self.analyzer.analyze(self.original)

        # Each token (key) has a term frequency (value)
        return Counter(tokens)
