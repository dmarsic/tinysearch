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
        {
            "text": "To be or not to be",
            "expected": ["to", "be", "or", "not", "to", "be"]
        }
    ]

    a = SimpleEnglishAnalyzer()
    for t in test_cases:
        tokens = a.analyze(t["text"])
        assert tokens == t["expected"]


def test_analyzer_with_stopwords():
    stopwords = {"and", "to", "be", "or", "not"}
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
                "haunt",
            ],  # this is based on the chosen stemmer
        },
        {
            "text": "To be or not to be",
            "expected": []
        }
    ]

    a = SimpleEnglishAnalyzer(stopwords)
    for t in test_cases:
        tokens = a.analyze(t["text"])
        assert tokens == t["expected"]
