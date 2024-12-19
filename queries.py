example_query = """
PREFIX ex: <http://example.org/>
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object .
}
"""

# Please Refer Readme for Dataset URL
# RDF Converstion is still in progress and converted data is not entirely reliable yet

# This gets all films in the same genre (genres from movies_metadata.rdf)
sameGenreQuery = ""

# This gets all ratings for the film (rating from ratings.rdf)
allRatingsQuery = ""

# This gets all films in the same collection (belongs_to_collection from movies_metadata.rdf)
sameCollectionQuery = ""

# This gets all films in the same category of Adult Movie or not (adult from movies_metadata.rdf)
sameAdultCatQuery = ""

# This gets all films with similar keywords (keywords from keywords.rdf)
sameKeyWordsQuery = ""