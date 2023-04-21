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


class Analyzer:
    def __init__(self):
        pass

    @classmethod
    def remove_nonchars(cls, token: str) -> str:
        m = re.search(r"[\w\-]+", token)
        if m:
            token = m.group(0)
        return token

    @classmethod
    def stem(cls, token: str) -> str:
        stemmer = Stemmer.Stemmer("english")
        return stemmer.stemWord(token)

    @classmethod
    def lower(cls, token: str) -> str:
        return token.lower()

    def analyze(self, text: str) -> List[str]:
        """Transforms input text to a list of tokens."""

        # Split on whitespace.
        tokens = re.split(r"\s+", text)

        # Apply transformations on each token.
        new_tokens = []
        for token in tokens:
            token = Analyzer.remove_nonchars(token)
            token = Analyzer.lower(token)
            token = Analyzer.stem(token)
            new_tokens.append(token)
        tokens = new_tokens
        return tokens
