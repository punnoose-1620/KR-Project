from rdflib import Graph

# SPARQL Query to find movies by director
givenDirectorQuery = """
PREFIX ns1: <http://example.org/ns1/>
SELECT ?title
WHERE {
    ?movie ns1:directedBy "George W. Hill" ;
           ns1:hasOriginalTitle ?title .
}
"""

def query_rdf_file(rdf_file, sparql_query):
    """
    Reads an RDF file, runs a SPARQL query, and prints the results.
    
    :param rdf_file: Path to the RDF file.
    :param sparql_query: The SPARQL query string to execute.
    """
    # Load the RDF file into a graph
    graph = Graph()
    try:
        graph.parse(rdf_file, format="turtle")  # Adjust format if needed
    except Exception as e:
        print(f"Error loading RDF file: {e}")
        return

    print(f"Loaded {len(graph)} triples.")
    
    # Run the SPARQL query
    try:
        results = graph.query(sparql_query)
        if len(results) == 0:
            print("No results found. Check query or data.")
        else:
            for result in results:
                print(result['title'])
    except Exception as e:
        print(f"Error executing SPARQL query: {e}")

    print("Query executed successfully.")

# File path
rdfFile = "./dataset_processed/MovieData.rdf"

# Execute the query
query_rdf_file(rdf_file=rdfFile, sparql_query=givenDirectorQuery)
