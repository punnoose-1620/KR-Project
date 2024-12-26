example_query = """
PREFIX ex: <http://example.org/>
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object .
}
"""

# Please Refer Readme for Dataset URL
# RDF Converstion is still in progress and converted data is not entirely reliable yet

# This gets all films containing given string in title. Return only films have the given string with hasOriginalTitle predicate
givenTitleQuery = ""

# This gets all films containing given genre. Return only films have the given genre with ofGenre predicate
givenGenreQuery = ""

# This gets all films in the given collection. Return only films have the given collection with partOfCollections predicate
givenCollectionQuery = ""

# This gets all films in the given category of Adult Movie or not. Return only films have the given True/False value for isAdult predicate
givenAdultCatQuery = ""

# This gets all films with given keyword. Return only films have the given keyword with hasKeywords predicate
givenKeyWordsQuery = ""

# This gets all films containing given actor. Return only films have the given actor with actedBy predicate
givenActorQuery = ""

# This gets all films containing given director. Return only films have the given director with directedBy predicate
givenDirectorQuery = """ PREFIX ns1: <http://example.org/property/>

SELECT ?movie ?title
WHERE {
    ?movie ns1:directedBy "Neil Jordan" ;
           ns1:hasOriginalTitle ?title .
}
  """

# This gets all films containing given producer. Return only films have the given producer with producedBy predicate
givenProducerQuery = ""

# This gets all films containing given writer. Return only films have the given writer with writtenBy predicate
givenWriterQuery = ""