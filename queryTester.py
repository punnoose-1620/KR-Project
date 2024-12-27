# To run with log, use the below command
# python .\queryTester.py > .\outputLogs\queryTestOutput.txt

import logging
from tqdm import tqdm
from queries import *
from constants import *
from rdflib import Graph

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
    for result in tqdm(results, desc="Parsing Results...."):
        print(result['title'])
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