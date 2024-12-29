# To run with log, use the below command
# python .\queryTester.py > .\outputLogs\queryTestOutput.txt

import json
import logging
from tqdm import tqdm
from queries import *
from constants import *
from rdflib import Graph

def resultsToJson(query_results):
    """
    Converts SPARQL query results into a list of JSON objects.
    
    :param query_results: SPARQL query results from rdflib's `Graph.query` method.
    :return: List of JSON objects with predicate as keys and object as values.
    """
    json_objects = []

    # Iterate through the SPARQL results
    for result in query_results:
        # Create a dictionary for each result
        json_obj = {}
        for var in result.labels.keys():
            value = result[var]
            if value is not None:
                json_obj[var] = str(value)  # Convert RDF terms to strings

        json_objects.append(json_obj)
        print("Converted Data Sample : ",json.dumps(json_objects[0], indent=4))
    return json_objects

def checkKeyValue(queryResults, key:str, value:str):
    existsCount = 0
    if len(queryResults)>0:
        for item in tqdm(queryResults, desc="Checking response queries...."):
            tempValue = str(item[key])
            if value in tempValue:
                existsCount = existsCount+1
    print(f"Result Length : Length of items with Value in Key\n{len(queryResults)}          : {existsCount}")

def query_rdf_file(rdf_file, sparql_query):
    """
    Reads an RDF file, runs a SPARQL query, and prints the results.
    
    :param rdf_file: Path to the RDF file.
    :param sparql_query: The SPARQL query string to execute.
    """
    # Load the RDF file into a graph
    graph = Graph()
    logging.info("Graph Loaded....")
    
    graph.parse(rdf_file, format="turtle")  # Adjust format if needed (e.g., 'xml', 'ntriples')
    print("Loaded Graph Size : ", len(graph))
    logging.info(f"Graph of length {len(graph)} Parsed....")
    # logging.info("Subject : Predicate : Object")
    # for s, p, o in graph:
    #     logging.info(f"{s} : {p} : {o}")
    
    # Run the SPARQL query
    results = graph.query(sparql_query)
    logging.info(f"Query : {sparql_query}")
    logging.info(f"Results of length {len(results)} obtained from Query")
    
    # Print results
    print("Results size : ",len(results))
    # for result in tqdm(results, desc="Parsing Results...."):
        # print(result)
    if len(results)>0:
        checkKeyValue("title", "Andrew Tiernan")
        jsonData = resultsToJson(results)
    print("Query executed successfully.")

if __name__=="__main__":
    logging.basicConfig(
        filename=queryTesterLog,
        level=logging.DEBUG,  # Set logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )
    logging.info("Query Tester Started....")
    query_rdf_file(rdf_file=rdfFile, sparql_query=getFilmByActor_Query("Andrew Tiernan"))
    logging.info("Query Tester Finished....")