import re
from collections import Counter

from tinysearch.analyzer import Analyzer


class Document:

    def __init__(self, original: str):
        self.original = original
        self.tokens = Counter()

    def __str__(self):
        return f'"{self.original}"'

    def analyze(self):
        a = Analyzer()
        tokens = a.analyze(self.original)

        # Each token (key) has a term frequency (value)
        self.tokens.update(tokens)
