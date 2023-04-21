import pytest
from tinysearch.search import Search


def test_search_empty_query():
    query = None
    with pytest.raises(ValueError):
        s = Search(["document1"], query)


def test_search():
    docs = [
        "Goldilocks and the Three Bears",
        "Fuzzy Wuzzy",
        "The Bear Went Over The Mountain",
        "We're Going on a Bear Hunt",
        "Brown Bear, Brown Bear, What Do You See?",
    ]
    query = "bear"
    expected_count = 3  # We don't stem so "bears" doesn't match
    expected_top_result = "Brown Bear, Brown Bear, What Do You See?"

    s = Search(docs, query)
    assert s.results.count == expected_count
    assert s.results.matches[0].doc.original == expected_top_result
