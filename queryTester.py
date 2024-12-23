from queries import *
from rdflib import Graph

def query_rdf_file(rdf_file, sparql_query):
    """
    Reads an RDF file, runs a SPARQL query, and prints the results.
    
    :param rdf_file: Path to the RDF file.
    :param sparql_query: The SPARQL query string to execute.
    """
    # Load the RDF file into a graph
    graph = Graph()
    graph.parse(rdf_file, format="turtle")  # Adjust format if needed (e.g., 'xml', 'ntriples')

    # Run the SPARQL query
    results = graph.query(sparql_query)

    # Print results
    for result in results:
        print(result)

    print("Query executed successfully.")

rdfFile = "./dataset_processed/MovieData.rdf"
query_rdf_file(rdf_file=rdfFile, sparql_query=example_query)