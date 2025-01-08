import json
from queries import *
from tqdm import tqdm
from constants import *
from rdflib import Graph, query
# This file has functions required to execute queries and get required movies

def runRdfQuery(rdf_file, sparql_query):
    # Load the RDF file into a graph
    graph = Graph()
    
    graph.parse(rdf_file, format="turtle")  # Adjust format if needed (e.g., 'xml', 'ntriples')
    
    # Run the SPARQL query
    results = graph.query(sparql_query)\
    
    # Print results
    if len(results)>0:
        jsonData = resultsToJson(results)
        return jsonData
    return []

def resultsToJson(query_results):
    json_objects = []
    mergedJsons = []

    def convertRdfToSPOjson():
        # Iterate through the SPARQL results
        for result in tqdm(query_results, desc="Creating JSON...."):
            # Create a dictionary for each result
            json_obj = {}
            testType = type(result)
            if not isinstance(result, dict):
                for var in result.labels.keys():
                    value = result[var]
                    if value is not None:
                        json_obj[var] = str(value)  # Convert RDF terms to strings

                json_objects.append(json_obj)
            else:
                # print(f"Rdf Result Instance : {type(result)} : {result}")
                mergedJsons.append(result)

    def unifySPOtoSingleObjects():
        temp_object = {}
        for item in json_objects:
            movieId = str(item['movie']).split('/')[-1]
            key = str(item['predicate']).split('/')[-1]
            value = item['object']
            # print(f"Sample Object : {movieId} : {key} : {value} : {temp_object}")
            if '_id' in temp_object.keys():
                if temp_object['_id']!=movieId:
                    mergedJsons.append(temp_object)
                    temp_object = {}
            if key in temp_object.keys():
                currentVal = temp_object[key]
                if isinstance(currentVal,list):
                    currentVal.append(value)
                    temp_object[key] = currentVal
                else:
                    temp_object[key] = [temp_object[key], value]
            temp_object[key] = value
        if temp_object!={}:
            mergedJsons.append(temp_object)

    print("Rdf Query Result Count : ",len(query_results))
    convertRdfToSPOjson()
    print("First Json Conversion Count : ", len(json_objects))
    if len(json_objects)>0:
        print("Sample First Json : ",json.dumps(json_objects[0],indent=4))
    unifySPOtoSingleObjects()
    print("Unified Json Conversion Count : ", len(mergedJsons))
    if len(mergedJsons)>0:
        print("Sample Unified Json : ",json.dumps(mergedJsons[0],indent=4))
    # mergeUnifiedObjectsToSingleJsonArr()
    return mergedJsons

def orderMoviesByRating(movies: list, tag:str=ascendingOrder):       # Tags: ASC, DESC
    itemKey = "avgRating"
    reverseFlag = False
    if tag=="DESC":
        reverseFlag = True
    movies = sorted(movies, key=lambda x: x.get(itemKey,0), reverse=reverseFlag)
    return movies
    print()

def getMovieByName(name: str):
    initialMoviesResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByTitle_Query(name))
    initialMovieJson = resultsToJson(initialMoviesResult)
    additionalNames = name.split(' ')
    additionalMovies = []
    for item in additionalNames:
        if item not in keywordsToIgnore:        # Make sure it is a relevant name
            additionalMoviesResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByTitle_Query(item))
            additionaMoviesJson = resultsToJson(additionalMoviesResult)
            for item in additionaMoviesJson:
                if item not in additionalMovies and item not in initialMovieJson:
                    additionalMovies.append(item)
    finalJson = {
        searchResultMovies: initialMovieJson,
        similarMovies: additionalMovies
    }
    return finalJson

def getMoviesByPersonBasic(name:str, role:str,queryType:str=similarQuery):
    returnObject = {}
    movies = []
    movies = getMoviesByPerson(name, role)
    returnObject[searchResultMovies] = movies
    if queryType==searchQuery:
        additionalNames = name.split(' ')
        for item in additionalNames:
            tempMovies = []
            for tempRole in rolesList:
                tempMovies = getMoviesByPerson(item, tempRole)
                if len(tempMovies)>0:
                    returnObject[similarMovies] = tempMovies
    return returnObject

def getMoviesByPerson(name: str, role:str=actorRole):         # Roles: ACTOR, DIRECTOR, WRITER, PRODUCER, ARTIST, EDITOR, SOUNDS, VISUALS, LIGHTING
    movies = []
    if role==actorRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByActor_Query(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==directorRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByDirector_Query(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==writerRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByWriter_Query(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==producerRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByProducer_Query(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==supportingArtistRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmBySupportingArtist(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==editorRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByEditor(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==soundsRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmBySounds(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==visualEffectsRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByVisualEffects(name))
        movies = resultsToJson(moviesByPersonResult)
    elif role==lightingRole:
        moviesByPersonResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByLighting(name))
        movies = resultsToJson(moviesByPersonResult)
    return movies

def getMovieByKeyWords(words: list):
    movies = []
    for word in words:
        if word not in keywordsToIgnore:
            # TODO: Get Movies with this word and append to movies
            wordSearchResults = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByKeyword_Query(keyword=word))
            wordSearchJson = resultsToJson(wordSearchResults)
            for movie in wordSearchJson:
                if movie not in movies:
                    movies.append(movie)
    return {searchResultMovies: movies}

def getMovieByCollection(name: str, queryType:str=similarQuery):
    returnObject = {}
    movies = []
    mainSearchResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByCollection_Query(collectionName=name))
    movies = resultsToJson(mainSearchResult)
    returnObject[searchResultMovies] = movies
    if queryType==searchQuery:
        tempMovies = []
        for item in name.split(' '):
            additionalSearchResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByCollection_Query(collectionName=item))
            additionalSearchJson = resultsToJson(additionalSearchResult)
            for film in additionalSearchJson:
                if film not in tempMovies:
                    tempMovies.append(film)
        if len(tempMovies)>0:
            returnObject[similarMovies] = tempMovies
    return returnObject

def getAdultMovies(flag:bool = False):
    movies = []
    mainSearchResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByAdultCat_Query(adultFlag=flag))
    movies = resultsToJson(mainSearchResult)
    return {searchResultMovies: movies}

def getMovieByGenre(genre: str):
    movies = []
    mainSearchResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByGenre_Query(genre=genre))
    movies = resultsToJson(mainSearchResult)
    return {searchResultMovies: movies}

def getMovieDetails(_id: str):
    mainSearchResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmById(_id=_id))
    movies = resultsToJson(mainSearchResult)
    if len(movies)>1:
        return {searchResultMovies: movies}
    else:
        return {searchResultMovies: movies[0]}