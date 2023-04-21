from pytest import fixture
from tinysearch.search import Search


@fixture
def docs():
    return [
        "I went to visit a farm one day",
        "Old McDonald had a farm",
        "One tomato, two tomatoes",
        "One, two, buckle my shoe",
        "Sleep, sleep, little one, sleep",
    ]


def test_integration(docs):
    queries = [
        {"query": "one", "results": 4, "top_result": "One tomato, two tomatoes"},
        {
            "query": "day one",
            "results": 4,
            "top_result": "I went to visit a farm one day",
        },
        {"query": "tomato", "results": 1, "top_result": "One tomato, two tomatoes"},
        {"query": "bear", "results": 0, "top_result": None},
    ]

    for q in queries:
        s = Search(docs, q["query"])
        print("Query:", q)
        print(s.results.matches)
        assert s.results.count == q["results"]
        if q["top_result"] is not None:
            assert s.results.matches[0].doc.original == q["top_result"]
        else:
            assert s.results.matches == []
