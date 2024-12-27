
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

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{titleKey}  "{title}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenTitleQuery

# This gets all films containing given genre. Return only films have the given genre with ofGenre predicate
def getFilmByGenre_Query(genre:str):
  givenGenreQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{genreKey}  "{genre}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenGenreQuery

# This gets all films in the given collection. Return only films have the given collection with partOfCollections predicate
def getFilmByCollection_Query(collectionName:str):
  givenCollectionQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{collectionsKey}  "{collectionName}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenCollectionQuery

# This gets all films in the given category of Adult Movie or not. Return only films have the given True/False value for isAdult predicate
def getFilmByAdultCat_Query(adultFlag:bool):
  adultAsString = str(adultFlag)
  givenAdultCatQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{adultKey}  "{adultAsString}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenAdultCatQuery

# This gets all films with given keyword. Return only films have the given keyword with hasKeywords predicate
def getFilmByKeyword_Query(keyword:str):
  givenKeyWordsQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{keywordsKey}  "{keyword}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenKeyWordsQuery

# This gets all films containing given actor. Return only films have the given actor with actedBy predicate
def getFilmByActor_Query(actor:str):
  givenActorQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{actorKey}  "{actor}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenActorQuery

# This gets all films containing given director. Return only films have the given director with directedBy predicate
def getFilmByDirector_Query(director: str):
  givenDirectorQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{directorKey}  "{director}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenDirectorQuery

# This gets all films containing given producer. Return only films have the given producer with producedBy predicate
def getFilmByProducer_Query(producer:str):
  givenProducerQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{producerKey}  "{producer}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenProducerQuery

# This gets all films containing given writer. Return only films have the given writer with writtenBy predicate
def getFilmByWriter_Query(writer:str):
  givenWriterQuery = f""" PREFIX ns1: <{sampleNameSpace}>

  SELECT ?movie ?title
  WHERE {{
      ?movie ns1:{writerKey}  "{writer}"   ;
            ns1:{titleKey} ?title .
  }}
    """
  return givenWriterQuery