from tinysearch.index import Index


def test_index_no_docs():
    docs = []
    expected_count = 0

    i = Index()
    i.index_docs(docs)
    assert len(i.docs) == expected_count


def test_index():
    docs = [
        "Goldilocks and the Three Bears",
        "Fuzzy Wuzzy",
        "The Bear Went Over The Mountain",
        "We're Going on a Bear Hunt",
        "Brown Bear, Brown Bear, What Do You See?",
    ]
    i = Index()
    i.index_docs(docs)
    assert len(i.docs) == len(docs)
    for n, doc in enumerate(docs):
        assert i.docs[n].original == doc
