"""Analyzer base.

A subclass can implement their own `analyze` method.
This base simply splits an input text on one or more spaces.

What happens in the analyze method is the implementation choice. In the
end, it needs to return a list of tokens.

Example usage:

    import re
    from tinysearch.base.analyzer import Analyzer

    class DashAnalyzer(Analyzer):
        def analyze(self, text: str) -> List[str]:
            tokens = self.dash_tokenizer(text)
            tokens = [t.lower for t in tokens]
            return tokens

        def dash_tokenizer(self, text: str) -> List[str]:
            return re.split("-", text)
"""

import re


class Analyzer:
    def __init__(self, stopwords: set[str] = set()):
        self.stopwords = stopwords

    def analyze(self, text: str) -> list[str]:
        return [token for token in re.split(r"\s+", text) if token.lower() not in self.stopwords]
