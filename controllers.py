import json
from queries import *
from tqdm import tqdm
from constants import *
from rdflib import Graph
# This file has functions required to execute queries and get required movies

def runRdfQuery(rdf_file, sparql_query):
    # Load the RDF file into a graph
    graph = Graph()
    # logging.info("Graph Loaded....")
    
    graph.parse(rdf_file, format="turtle")  # Adjust format if needed (e.g., 'xml', 'ntriples')
    # logging.info(f"Graph of length {len(graph)} Parsed....")
    
    # Run the SPARQL query
    results = graph.query(sparql_query)
    # logging.info(f"Query : {sparql_query}")
    # logging.info(f"Results of length {len(results)} obtained from Query")
    
    # Print results
    if len(results)>0:
        jsonData = resultsToJson(results)
        return jsonData
    return []

def resultsToJson(query_results):
    json_objects = []
    # Iterate through the SPARQL results
    for result in tqdm(query_results, desc="Creating JSON...."):
        # Create a dictionary for each result
        json_obj = {}
        for var in result.labels.keys():
            value = result[var]
            if value is not None:
                json_obj[var] = str(value)  # Convert RDF terms to strings

        json_objects.append(json_obj)

    unified_json = {}           # values are of format { movieId: movieDetailsObject }
    for item in tqdm(json_objects, desc="Unifying JSON based on ID...."):
        itemId = str(item['movie']).split('/')[-1]
        ref_keys = list(item.keys())
        ref_keys.remove('movie')
        if itemId in unified_json.keys():
            itemVal = unified_json[itemId]
            for key in ref_keys:
                if item[key]!=itemVal[key]:
                    if not isinstance(itemVal[key],list):
                        itemVal[key] = [itemVal[key]]
                    itemVal[key].append(item[key])
            unified_json[itemId] = itemVal
        else:
            itemVal = {
                '_id': itemId,
            }
            for key in ref_keys:
                itemVal[key] = item[key]
            unified_json[itemId] = itemVal
        # print("Converted Data Sample : ",json.dumps(json_objects[0], indent=4))
    
    finalizedJson = []          # values are of format [movieDetailsObject1, movieDetailsObject2,....]
    for key in tqdm(unified_json.keys(), desc="Finalizing JSON Conversion"):
        value = unified_json[key]
        finalizedJson.append(value)

    # print("Converted Data Sample : ",json.dumps(finalizedJson[0], indent=4))
    return finalizedJson

def orderMoviesByRating(movies: list, tag:str=ascendingOrder):       # Tags: ASC, DESC
    itemKey = "avgRating"
    reverseFlag = False
    if tag=="DESC":
        reverseFlag = True
    movies = sorted(movies, key=lambda x: x.get(itemKey,0), reverse=reverseFlag)
    return movies
    print()

def getMovieByName(name: str):
    initialMoviesResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByTitle_Query(item))
    initialMovieJson = resultsToJson(initialMoviesResult)
    additionalNames = name.split(' ')
    additionalMovies = []
    for item in additionalNames:
        if item not in keywordsToIgnore:        # Make sure it is a relevant name
            additionalMoviesResult = runRdfQuery(rdf_file=rdfFile, sparql_query=getFilmByTitle_Query(item))
            additionaMoviesJson = resultsToJson(additionalMoviesResult)
            for item in additionaMoviesJson:
                if item not in additionalMovies:
                    additionalMovies.append(item)
    finalJson = {
        searchResultMovies: initialMovieJson,
        similarMovies: additionalMovies
    }
    return finalJson

def getMoviesByPersonBasic(name:str, role:str,queryType:str=similarQuery):
    returnObject = {}
    movies = []
    # TODO: Get movies for Exact Person and add to movies
    movies = getMovieByName(name, role)
    returnObject[searchResultMovies] = movies
    if queryType==searchQuery:
        # TODO: Get Person with similar names
        additionalNames = name.split(' ')
        for item in additionalNames:
            tempMovies = []
            for tempRole in rolesList:
                tempMovies = getMoviesByPerson(item, tempRole)
                if len(tempMovies)>0:
                    returnObject[similarMovies] = tempMovies
    return returnObject

def getMoviesByPerson(name: str, role:str=actorRole):         # Roles: ACTOR, DIRECTOR, WRITER, PRODUCER, ARTIST, EDITOR, SOUNDS, VISUALS, LIGHTING
    # TODO: Gets movies for the exact name specified
    movies = []
    if role==actorRole:
        print()
    elif role==directorRole:
        print()
    elif role==writerRole:
        print()
    elif role==producerRole:
        print()
    elif role==supportingArtistRole:
        print()
    elif role==editorRole:
        print()
    elif role==soundsRole:
        print()
    elif role==visualEffectsRole:
        print()
    elif role==lightingRole:
        print()
    return movies

def getMovieByKeyWords(words: list):
    movies = []
    for word in words:
        if word not in keywordsToIgnore:
            # TODO: Get Movies with this word and append to movies
            print()
    return movies

def getMovieByCollection(name: str, queryType:str=similarQuery):
    returnObject = {}
    movies = []
    # TODO: Get movies under exact collection name
    returnObject[searchResultMovies] = movies
    if queryType==searchQuery:
        tempMovies = []
        # TODO: Get movies with similar collection names
        if len(tempMovies)>0:
            returnObject[similarMovies] = tempMovies
        print()
    print()

def getAdultMovies(flag:bool = False):
    movies = []
    # TODO: Get movies from the same Adult Category
    return movies

def getMovieByGenre(genre: str):
    movies = []
    # TODO: Get movies from given genre into movies list
    return movies

def getMoviewDetails(_id: str):
    movieDetails = {}
    # TODO: Get details of movies with given ID
    return movieDetails