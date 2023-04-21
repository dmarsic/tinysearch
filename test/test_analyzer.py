from tinysearch.analyzer import SimpleEnglishAnalyzer


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
            "expected": [
                "audaci",
                "origin",
                "and",
                "haunt",
            ],  # this is based on the chosen stemmer
        },
    ]

    a = SimpleEnglishAnalyzer()
    for t in test_cases:
        tokens = a.analyze(t["text"])
        assert tokens == t["expected"]
