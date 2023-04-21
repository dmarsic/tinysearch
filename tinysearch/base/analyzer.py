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
from typing import List


class Analyzer:
    def analyze(self, text: str) -> List[str]:
        return re.split(r"\s+", text)
