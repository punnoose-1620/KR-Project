from constants import *
# This file has functions required to execute queries and get required movies

def orderMoviesByRating(movies: list, tag:str=ascendingOrder):       # Tags: ASC, DESC
    print()

def getMovieByName(name: str):
    # TODO: Get Exact Movie Name
    additionalNames = name.split(' ')
    for item in additionalNames:
        if item not in keywordsToIgnore:        # Make sure it is a relevant name
            # TODO: Get additional movies with similar titles
            print()
    print()

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