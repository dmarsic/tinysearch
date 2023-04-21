from tinysearch.analyzer import Analyzer


def test_analyzer():
    test_cases = [
        {
            "text": "",
            "expected": [""],
        },
        {
            "text": "hello!",
            "expected": ["hello"],
        },
        {
            "text": "Audacious, original and haunting",
            "expected": ["audacious", "original", "and", "haunting"],
        },
    ]

    a = Analyzer()
    for t in test_cases:
        tokens = a.analyze(t["text"])
        assert tokens == t["expected"]
