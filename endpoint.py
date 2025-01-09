#!/usr/bin/env python
# coding: utf-8

# API Endpoint file

# To run as server on linux
# uvicorn main:app --port 5000 --reload

# To run as server on windows
# python -m uvicorn main:app --port 5000 --reload

import json
import socket
import uvicorn
import logging
from classes import *
from constants import *
from controllers import *
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Knowledge Representation Project Server",
    summary="Python Server for the Knowledge Representation Project"
)

if __name__ == '__main__':
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)
    log_config = uvicorn.config.LOGGING_CONFIG
    # log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run(
        'endpoint:app', 
        port=portNumber, 
        reload=True, 
        workers=1, 
        host=ipAddress,
        log_config=log_config
        )
    logging.basicConfig(
        filename=endpointLog,
        level=logging.DEBUG,  # Set logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )
    logging.info("Backend API Endpoint Initialized....")
    logging.info(f"Base Url : https://{ipAddress}:{portNumber}/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

@app.post("/search-by-name")
def searchByName(input: NameFromUser):
    logging.info("Search By Name Invoked....")
    logging.info(f"Search By Name Input Data : {json.dumps(input.getJson(), indent=4)}")
    print("Input Data : ",json.dumps(input.getJson()))
    result = getMovieByName(name=input.name)
    print("Response Data : ",json.dumps(result))
    logging.info(f"Search By Name Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/search-by-person")
def searchByPerson(input: PersonFromUser):
    logging.info("Search By Person Invoked....")
    logging.info(f"Search By Person Input Data : {json.dumps(input.getJson(), indent=4)}")
    result = getMoviesByPersonBasic(name=input.person, role=input.role, queryType=input.queryType)
    logging.info(f"Search By Person Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/search-by-keyword")
def searchByKeyWord(input: KeyWordsFromUser):
    logging.info("Search By Keyword Invoked....")
    logging.info(f"Search By Keyword Input Data : {json.dumps(input.getJson(), indent=4)}")
    result = getMovieByKeyWords(words=input.keywords)
    logging.info(f"Search By Keyword Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/search-by-collection")
def searchByCollection(input: NameFromUser):
    logging.info("Search By Collection Invoked....")
    logging.info(f"Search By Collection Input Data : {json.dumps(input.getJson(), indent=4)}")
    result = getMovieByCollection(name=input.name)
    logging.info(f"Search By Collection Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/search-by-adult-category")
def searchByAdultCategory(input: FlagFromUser):
    logging.info("Search By Adult Category Invoked....")
    logging.info(f"Search By Adult Category Input Data : {json.dumps(input.getJson(), indent=4)}")
    result = getAdultMovies(flag=input.flag)
    logging.info(f"Search By Adult Category Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/search-by-genre")
def searchByGenre(input: NameFromUser):
    logging.info("Search By Genre Invoked....")
    logging.info(f"Search By Genre Input Data : {json.dumps(input.getJson(), indent=4)}")
    result = getMovieByGenre(genre=input.name)
    logging.info(f"Search By Genre Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)

@app.post("/get-movie-details")
def getDetails(input: IdFromUser):
    logging.info("Get Movie Details Invoked....")
    logging.info(f"Get Movie Details Input Data : {json.dumps(input.getJson(), indent=4)}")
    print("Get Movie Details Request Body : ",json.dumps(input.getJson(), indent=4))
    result = getMovieDetails(_id=input.movieId)
    print("Get Movie Details Response : ",json.dumps(result, indent=4))
    logging.info(f"Get Movie Details Response Data : {json.dumps(result, indent=4)}")
    return json.dumps(result, indent=4)