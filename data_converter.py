import os
import csv
import kagglehub
from tqdm import tqdm
from rdflib import Graph, URIRef, Literal, Namespace

kaggle_dataset = "rounakbanik/the-movies-dataset"
output_folder = "dataset_processed"

def read_csv(singleFilePath:str, outputFilePath:str):
    try:
        with open(singleFilePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            write_to_rdf(csv_reader, outputFilePath)

    except FileNotFoundError:
        print(f"The file '{singleFilePath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_rdf(csvData, rdfPath, base_uri="http://example.org/"):
    # Create an RDF graph
    graph = Graph()
    ns = Namespace(base_uri)

    # Extract headers as predicates
    headers = next(csvData, None)
    if not headers:
        print("CSV file is empty or missing headers.")
        return

    # Generate RDF triples for each row
    for i, row in tqdm(enumerate(csvData), desc="Creating RDF Triples "):
        subject = URIRef(f"{base_uri}row/{i+1}")
        for header, value in zip(headers, row):
            predicate = URIRef(f"{base_uri}{header.strip()}")
            graph.add((subject, predicate, Literal(value)))

    # Serialize the RDF graph to a file
    graph.serialize(destination=rdfPath, format="turtle")
    rdfFileName = str(rdfPath).split("\\")
    print(f"RDF data has been written to {rdfFileName[-1]}\n")

def list_files_in_folder(folder_path):
    file_names = []
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        # print("File : Path")
        for file in files:
            if file not in ('ratings_small.csv', 'links_small.csv'):
                file_path = os.path.join(root, file)
                output_file = file.replace(".csv",'.rdf')
                output_file_path = os.path.join(output_folder,output_file)
                file_names.append(files)
                # print(file," : ",file_path)
                read_csv(file_path, output_file_path)

# Get Files from Kaggle
path = kagglehub.dataset_download(kaggle_dataset)
print("Path to dataset temporary files:", path)

list_files_in_folder(path)