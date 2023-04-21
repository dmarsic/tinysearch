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
from typing import List


class Analyzer:
    def __init__(self):
        pass

    def analyze(self, text: str) -> List[str]:
        """Transforms input text to a list of tokens."""

        # Split on whitespace.
        tokens = re.split(r"\s+", text)

        # Remove all but letters, numbers, and dashes.
        new_tokens = []
        for token in tokens:
            m = re.search(r"[\w\-]+", token)
            if m:
                token = m.group(0)
            new_tokens.append(token)
        tokens = new_tokens

        # Lowercase.
        tokens = [token.lower() for token in tokens]

        return tokens
