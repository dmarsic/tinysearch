import pytest

from tinysearch.document import Document


def test_nil_document():
    text = None
    with pytest.raises(ValueError):
        d = Document(text)


def test_document():
    test_cases = [
        {"text": "", "expected": [""]},
        {"text": "foo", "expected": ["foo"]},
        {
            "text": "There should be one-- and preferably only one --obvious way to do it.",
            "expected": [
                "there",
                "should",
                "be",
                "one--",
                "and",
                "preferably",
                "only",
                "one",
                "--obvious",
                "way",
                "to",
                "do",
                "it",
            ],
        },
    ]

    for t in test_cases:
        d = Document(t["text"])
        assert list(d.tokens.keys()) == t["expected"]
