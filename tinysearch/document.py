"""Document represents a document to be indexed and searched.

Example usage:

    t = "There was the distinct sound of the tavern door smashing open."
    d = Document(t)
    d.analyze()

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

from tinysearch.analyzer import Analyzer


class Document:
    """Document that can be indexed and searched.

    Document is instantiated with the text value of a document.
    It can be parsed or analyzed, which produces a tokenized
    list (also called terms).
    """
    def __init__(self, original: str):
        self.original = original
        self.tokens = Counter()

    def __str__(self):
        return f'"{self.original}"'

    def analyze(self):
        """Parses the original text into a list of tokens."""
        a = Analyzer()
        tokens = a.analyze(self.original)

        # Each token (key) has a term frequency (value)
        self.tokens.update(tokens)
