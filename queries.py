
from constants import *

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


def getFilmByTitle_Query(title:str):
  givenTitleQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{titleKey} ?title ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?title), LCASE("{title}")))
}}"""
  return givenTitleQuery



# This gets all films containing given genre. Return only films have the given genre with ofGenre predicate

def getFilmByGenre_Query(genre:str):
  givenGenreQuery =f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{genreKey} ?genre ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?genre), LCASE("{genre}")))
}}"""
  return givenGenreQuery

# This gets all films in the given collection. Return only films have the given collection with partOfCollections predicate


def getFilmByCollection_Query(collectionName:str):
  givenCollectionQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{collectionsKey} ?collectionName ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?collectionName), LCASE("{collectionName}")))
}}"""
  return givenCollectionQuery

# This gets all films in the given category of Adult Movie or not. Return only films have the given True/False value for isAdult predicate
def getFilmByAdultCat_Query(adultFlag:bool):
  adultAsString = str(adultFlag)
  givenAdultCatQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{adultKey} ?adult ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?adult), LCASE("{adultAsString}")))
}}"""
  return givenAdultCatQuery

# This gets all films with given keyword. Return only films have the given keyword with hasKeywords predicate
def getFilmByKeyword_Query(keyword:str):
  givenKeyWordsQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{keywordsKey} ?keyword ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?keyword), LCASE("{keyword}")))
}}"""
  return givenKeyWordsQuery

# This gets all films containing given actor. Return only films have the given actor with actedBy predicate
def getFilmByActor_Query(actor:str):
  givenActorQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{actorKey} ?actor ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?actor), LCASE("{actor}")))
}}"""
  return givenActorQuery

# This gets all films containing given director. Return only films have the given director with directedBy predicate
def getFilmByDirector_Query(director: str):
  givenDirectorQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{directorKey} ?director ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?director), LCASE("{director}")))
}}"""
  return givenDirectorQuery

# This gets all films containing given producer. Return only films have the given producer with producedBy predicate
def getFilmByProducer_Query(producer:str):
  givenProducerQuery =f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{producerKey} ?producer ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?producer), LCASE("{producer}")))
}}"""
  return givenProducerQuery

# This gets all films containing given writer. Return only films have the given writer with writtenBy predicate
def getFilmByWriter_Query(writer:str):
  givenWriterQuery = f""" PREFIX ns1: <{sampleNameSpace}>

SELECT DISTINCT ?movie ?predicate ?object
WHERE {{
    ?movie ns1:{writerKey} ?writer ;
           ?predicate ?object .
    FILTER(CONTAINS(LCASE(?writer), LCASE("{writer}")))
}}"""
  return givenWriterQuery