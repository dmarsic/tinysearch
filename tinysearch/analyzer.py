import re
from typing import List


class Analyzer:
    def __init__(self):
        pass

    def analyze(self, text: str) -> List[str]:
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


