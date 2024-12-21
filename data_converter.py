import os
import csv
import json
import kagglehub
from tqdm import tqdm
from datetime import datetime
from rdflib import Graph, URIRef, Literal, Namespace

kaggle_dataset = "rounakbanik/the-movies-dataset"
output_folder = "dataset_processed"
jsonMovieData = []
startTime = datetime.now()
endTime = datetime.now()

def readCredits(filePath: str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Credits Read with headers : ",headers)
            creditsCount = 0
            for row in tqdm(csv_reader, desc="Reading Credits"):
                creditsCount = creditsCount+1
                cast = row[0]
                crew = row[1]
                _id = row[2]
                foundFlag = False
                for item in jsonMovieData:
                    if item['_id']==_id:
                        foundFlag = True
                        item['castList'] = cast
                        item['crewList'] = crew
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'castList' : cast,
                        'crewList' : crew
                    }
                    jsonMovieData.append(movie_data)
            print("Credits Entries read : ",creditsCount)

    except FileNotFoundError:
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readKeyWords(filePath: str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("KeyWords Read with headers : ",headers)
            keywordsCount = 0
            for row in tqdm(csv_reader, desc="Reading KeyWords"):
                keywordsCount = keywordsCount+1
                _id = row[0]
                keywordsObjects = row[1]
                keywords = []
                for item in keywordsObjects:
                    if not isinstance(item,str):
                        word = item['name']
                        if word not in keywords:
                            keywords.append(word)
                foundFlag = False
                for item in jsonMovieData:
                    if item['_id']==_id:
                        foundFlag = True
                        item['keywords'] = keywords
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'keywords' : keywords
                    }
                    jsonMovieData.append(movie_data)
            print("Keywords Entries read : ",keywordsCount)

    except FileNotFoundError:
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readLinks(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Links Read with headers : ",headers)
            linksCount = 0
            for row in tqdm(csv_reader, desc="Reading Links"):
                linksCount = linksCount+1
                _id = row[0]
                imdbId = row[1]
                tmdbId = row[2]
                foundFlag = False
                for item in jsonMovieData:
                    if item['_id']==_id:
                        foundFlag = True
                        item['imdbId'] = imdbId
                        item['tmdbId'] = tmdbId
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'imdbId' : imdbId,
                        'tmdbId' : tmdbId
                    }
                    jsonMovieData.append(movie_data)
            print("Links Entries read : ",linksCount)


    except FileNotFoundError:
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readMetaData(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("MetaData Read with headers : ",headers)
            duplicateOverwrites = 0
            metaDataCount = 0
            for row in tqdm(csv_reader, desc="Reading MetaData"):
                metaDataCount = metaDataCount+1
                adult = row[0]
                collectionDataObject = row[1]
                collectionDataList = []
                for item in collectionDataObject:
                    if len(str(item).strip())!=0 and item!='':
                        title = item['name']
                        if title not in collectionDataList:
                            collectionDataList.append(title)
                budget = row[2]
                genresObject = row[3]
                genresList = []
                for item in genresObject:
                    title = item['name']
                    if title not in genresList:
                        genresList.append(title)
                homePage = row[4]
                _id = row[5]
                imdbId = row[6]
                originalLang = row[7]
                originalTitle = row[8]
                overview = row[9]
                foundFlag = False
                for item in jsonMovieData:
                    if item['_id']==_id or item['imdbId']==imdbId:
                        foundFlag = True
                        if item['isAdult']!=None:
                            duplicateOverwrites = duplicateOverwrites+1
                        item['isAdult'] = adult
                        item['partOfCollections'] = collectionDataList
                        item['budget'] = budget
                        item['genres'] = genresList
                        item['originalLanguage'] = originalLang
                        item['originalTitle'] = originalTitle
                        item['overview'] = overview
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'isAdult' : adult,
                        'partOfCollections' : collectionDataList,
                        'budget' : budget,
                        'genres' : genresList,
                        'originalLanguage' : originalLang,
                        'originalTitle' : originalTitle,
                        'overview' : overview
                    }
                    jsonMovieData.append(movie_data)
            print("Duplicate MetaData Count : ", duplicateOverwrites)
            print("MetaData Entries read : ",metaDataCount)

    except FileNotFoundError:
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def readRatings(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Ratings Read with headers : ",headers)
            ratingsCount = 0
            for row in tqdm(csv_reader, desc="Reading Ratings"):
                ratingsCount = ratingsCount+1
                userId = row[0]
                _id = row[1]
                rating = row[2]
                timeStamp = row[3]
                foundFlag = False
                for item in jsonMovieData:
                    if (item['_id']==_id) and ('rating' in item.keys()):
                        foundFlag = True
                        temp_rating = item['rating']
                        temp_rating.append(rating)
                        item['rating'] = temp_rating
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'rating' : [rating]
                    }
                    jsonMovieData.append(movie_data)
            print("Rating Entries read : ",ratingsCount)

    except FileNotFoundError:
        print(f"The file '{filePath}' does not exist.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

def printSampleJsonData(printType:str):
    sampleData = jsonMovieData[0]
    if printType=='value':
        print("\nSample Data : ", end=None)
        print(json.dumps(sampleData,indent=4))
    else:
        typesData = {}
        keys = list(sampleData.keys())
        for key in keys:
            typesData[key] = str(type(sampleData[key]))
        print("Data Types : ", end=None)
        print(json.dumps(typesData, indent=4), end="\n\n")

def writeToJson(outputFile: str):
    try:
        with open(outputFile, mode='w', encoding='utf-8') as file:
            json.dump(jsonMovieData, file, indent=4, ensure_ascii=False)
        print(f"JSON data has been written to {outputFile}")
    except TypeError as e:
        print(f"Error: Provided data is not JSON serializable. {e}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def list_files_in_folder(folder_path):
    file_names = []
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file not in ('ratings_small.csv', 'links_small.csv'):
                file_names.append(file)
                filePath = os.path.join(root,file)
                if 'credits.csv' in file:
                    readCredits(filePath=filePath)
                elif 'keywords.csv' in file:
                    readKeyWords(filePath=filePath)
                elif 'links.csv' in file:
                    readLinks(filePath=filePath)
                elif 'movies_metadata.csv' in file:
                    readMetaData(filePath=filePath)
                elif 'ratings.csv' in file:
                    readRatings(filePath=filePath)
                print("Current Json Structure : ", end=None)
                printSampleJsonData('types')
    print("Unified Data Count : ",jsonMovieData.count())
    printSampleJsonData('types')
    output_file_path = os.path.join(output_folder,"JsonData.json")
    writeToJson(outputFile=output_file_path)
    print("\nFiles Processed : ", file_names)         

# Get Files from Kaggle
path = kagglehub.dataset_download(kaggle_dataset)
print("Path to dataset temporary files:", path)

list_files_in_folder(path)
endTime = datetime.now()
delta = endTime-startTime
min_delta = round(delta.total_seconds()/60, ndigits=None)
sec_delta = delta.total_seconds() - (min_delta*60)
print("Convertion time : ",min_delta," minutes and ",sec_delta," seconds")