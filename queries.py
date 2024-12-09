example_query = """
PREFIX ex: <http://example.org/>
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object .
}
"""