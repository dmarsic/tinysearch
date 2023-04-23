"""
Analyzer transforms input text into a token list.

It has a single public method: analyze

Example usage:

    a = Analyzer()

    text = "Audacious, original and haunting"
    tokens = a.analyze(text)

    # tokens = ["audacious", "original", "and", "haunting"]
"""

import re
import Stemmer
from typing import List

from tinysearch.base.analyzer import Analyzer


class SimpleEnglishAnalyzer(Analyzer):
    def __init__(self):
        super().__init__()
        self.stemmer = Stemmer.Stemmer("english")

    @classmethod
    def remove_nonchars(cls, token: str) -> str:
        new_chars = []
        for c in token:
            if c.isalnum() or c == "-":
                new_chars.append(c)
        return ''.join(new_chars)

    @classmethod
    def lower(cls, token: str) -> str:
        return token.lower()

    def stem(self, token: str) -> str:
        return self.stemmer.stemWord(token)

    def analyze(self, text: str) -> List[str]:
        """Transforms input text to a list of tokens."""

        # Split on whitespace.
        tokens = re.split(r"\s+", text)

        # Apply transformations on each token.
        new_tokens = []
        for token in tokens:
            token = self.remove_nonchars(token)
            token = self.lower(token)
            token = self.stem(token)
            new_tokens.append(token)
        tokens = new_tokens
        return tokens
