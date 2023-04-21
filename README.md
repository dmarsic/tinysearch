# TinySearch

TinySearch is a tiny one-phase search engine. It is extremely easy to use
and works well with simple lists where the query may not match the document
text exactly.

This is a minimal search engine. You don't need to run a separate, big instances of search engine when your use case is a few hundreds or thousands small documents.

## Example

Input documents:

```
"Goldilocks and the Three Bears"
"Fuzzy Wuzzy"
"The Bear Went Over The Mountain"
"We're Going on a Bear Hunt"
"Brown Bear, Brown Bear, What Do You See?"
```

Search query:

```
bear
```

Results (ordered by best match):

```
"Brown Bear, Brown Bear, What Do You See?"
"The Bear Went Over The Mountain"
"We're Going on a Bear Hunt"
```

## How to use

```python
from tinysearch.search import Search

docs = [
    "Goldilocks and the Three Bears",
    "Fuzzy Wuzzy",
    "The Bear Went Over The Mountain",
    "We're Going on a Bear Hunt",
    "Brown Bear, Brown Bear, What Do You See?",
]
query = "bear"

s = Search(docs, query)

# How many results?
print(s.results.count)

# What is the top result?
print(s.results.matches[0].doc)

# Print all matches. Best results are at the top.
for m in s.results.matches:
    print(m.doc)
```

## Under the hood

When you pass documents to the `Search` object, each document is
tokenized and transformed for easier search. The same process is
applied to the query.

Then each document is scored using the TF-IDF algorithm to find the best
match, and matches are returned sorted to the user. The best match is
at the top.

## License

See LICENSE.
