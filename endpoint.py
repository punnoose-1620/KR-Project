#!/usr/bin/env python
# coding: utf-8

# API Endpoint file

# To run as server on linux
# uvicorn main:app --port 5000 --reload

# To run as server on windows
# python -m uvicorn main:app --port 5000 --reload

import json
from classes import *
from constants import *
from controllers import *
import logging
import sys
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Knowledge Representation Project Server",
    summary="Python Server for the Knowledge Representation Project"
)

if __name__ == '__main__':
    uvicorn.run('endpoint:app', port=5000, reload=True, workers=1)  # , host='192.168.0.84'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

@app.get("/search-by-name")
def searchByName(input: NameFromUser):
    result = getMovieByName(name=input.name)
    return json.dumps(result, indent=4)

@app.get("/search-by-person")
def searchByPerson(input: PersonFromUser):
    result = getMoviesByPersonBasic(name=input.person, role=input.role, queryType=input.queryType)
    return json.dumps(result, indent=4)

@app.get("/search-by-keyword")
def searchByKeyWord(input: KeyWordsFromUser):
    result = getMovieByKeyWords(words=input.keywords)
    return json.dumps(result, indent=4)

@app.get("/search-by-collection")
def searchByCollection(input: NameFromUser):
    result = getMovieByCollection(name=input.name)
    return json.dumps(result, indent=4)

@app.get("/search-by-adult-category")
def searchByAdultCategory(input: FlagFromUser):
    result = getAdultMovies(flag=input.flag)
    return json.dumps(result, indent=4)

@app.get("/search-by-genre")
def searchByGenre(input: NameFromUser):
    result = getMovieByGenre(genre=input.name)
    return json.dumps(result, indent=4)

@app.get("/get-movie-details")
def getDetails(input: IdFromUser):
    result = getMovieDetails(_id=input.movieId)
    return json.dumps(result, indent=4)