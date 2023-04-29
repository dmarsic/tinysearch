"""
Analyzer transforms input text into a token list.

It has a single public method: analyze

analyze method will be called a lot, it needs to be optimized for
performance as much as possible.

Example usage:

    a = Analyzer()

    text = "Audacious, original and haunting"
    tokens = a.analyze(text)

    # tokens = ["audacious", "original", "and", "haunting"]
"""

import re
import Stemmer

from tinysearch.base.analyzer import Analyzer


class SimpleEnglishAnalyzer(Analyzer):
    def __init__(self, stopwords: set[str] = set()):
        super().__init__(stopwords)
        self.stemmer = Stemmer.Stemmer("english")

    @classmethod
    def remove_nonchars(cls, token: str) -> str:
        return "".join([c for c in token if c.isalnum() or c == "-"])

    @classmethod
    def lower(cls, token: str) -> str:
        return token.lower()

    def stem(self, token: str) -> str:
        return self.stemmer.stemWord(token)

    def analyze(self, text: str) -> list[str]:
        """Transforms input text to a list of tokens."""

        # Split on whitespace.
        tokens = re.split(r"\s+", text)

        # Apply transformations on each token.
        return [self.stem(self.lower(self.remove_nonchars(token))) for token in tokens if self.lower(token) not in self.stopwords]
