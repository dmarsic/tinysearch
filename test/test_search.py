import pytest
from tinysearch.index import Index
from tinysearch.search import Search

@pytest.fixture
def docs():
    return [
        "Goldilocks and the Three Bears",
        "Fuzzy Wuzzy",
        "The Bear Went Over The Mountain",
        "We're Going on a Bear Hunt",
        "Brown Bear, Brown Bear, What Do You See?",
    ]


def test_search_empty_query():
    query = None
    with pytest.raises(ValueError):
        s = Search(["document1"])
        s.search(query)


def test_search(docs):
    query = "bear"
    expected_count = 4  # use of stemming ensures that bear and bears have the same stem
    expected_top_result = "Brown Bear, Brown Bear, What Do You See?"

    s = Search(docs)
    s.search(query)
    assert s.results.count == expected_count
    assert s.results.matches[0].doc.original == expected_top_result


def test_search_with_indexing_first(docs):
    query = "bear"
    expected_count = 4  # use of stemming ensures that bear and bears have the same stem
    expected_top_result = "Brown Bear, Brown Bear, What Do You See?"

    i = Index()
    i.index_docs(docs)
    s = Search(i)
    s.search(query)
    assert s.results.count == expected_count
    assert s.results.matches[0].doc.original == expected_top_result
