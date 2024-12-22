import os
import csv
import json
import logging
import kagglehub
from tqdm import tqdm
from datetime import datetime
from rdflib import Graph, URIRef, Literal, Namespace

kaggle_dataset = "rounakbanik/the-movies-dataset"
output_folder = "dataset_processed"
jsonMovieData = []
startTime = datetime.now()
endTime = datetime.now()

# Functions to read each individual CSV file and add relevant parameters to JSON data variable
 
def readCredits(filePath: str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            logging.info("Credits file opened....")
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Credits Read with headers : ",headers)
            logging.info(f"Credits headers : {headers}")
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
            logging.info(f"Credits count : {creditsCount}")

    except FileNotFoundError:
        logging.error(f"Credits error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"Credits error : {e}")
        print(f"An error occurred: {e}")

def readKeyWords(filePath: str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            logging.info("KeyWords file opened....")
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("KeyWords Read with headers : ",headers)
            logging.info(f"KeyWords headers : {headers}")
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
                        item['hasKeywords'] = keywords
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'hasKeywords' : keywords
                    }
                    jsonMovieData.append(movie_data)
            print("Keywords Entries read : ",keywordsCount)
            logging.info(f"KeyWords count : {keywordsCount}")

    except FileNotFoundError:
        logging.error(f"KeyWords error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"KeyWords error : {e}")
        print(f"An error occurred: {e}")

def readLinks(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            logging.info("Links file opened....")
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Links Read with headers : ",headers)
            logging.info(f"Links headers : {headers}")
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
            logging.info(f"Links count : {linksCount}")


    except FileNotFoundError:
        logging.error(f"Links error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"Links error : {e}")
        print(f"An error occurred: {e}")

def readMetaData(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            logging.info("MetaData file opened....")
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("MetaData Read with headers : ",headers)
            logging.info(f"MetaData headers : {headers}")
            duplicateOverwrites = 0
            metaDataCount = 0
            object_corrector_flag = False
            for row in tqdm(csv_reader, desc="Reading MetaData"):
                metaDataCount = metaDataCount+1
                adult = row[0]
                collectionDataObject = row[1]
                collectionDataList = []
                for item in collectionDataObject:
                    if (not isinstance(item, str)) and (len(item)>0):
                        title = item['name']
                        if title not in collectionDataList:
                            collectionDataList.append(title)
                budget = row[2]
                genresObject = row[3]
                if isinstance(genresObject, str) and ('{' in genresObject) and ('}' in genresObject):
                    printVal = "Damn"
                    if object_corrector_flag==True:
                        printVal = "n"
                    if (genresObject[0]=="'") and (genresObject[-1]=="'"):
                        object_corrector_flag = True
                        print(printVal, end=None)
                    genresObject = json.loads(str(genresObject).replace("'",'"'))
                    if object_corrector_flag==True:
                        print(" Girl....\n")
                genresList = []
                for item in genresObject:
                    if not isinstance(item, str):
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
                    if item['_id']==_id:
                        foundFlag = True
                        if 'isAdult' in item.keys():
                            duplicateOverwrites = duplicateOverwrites+1
                        item['isAdult'] = adult
                        item['partOfCollections'] = collectionDataList
                        item['hasBudget'] = budget
                        item['ofGenre'] = genresList
                        item['hasOriginalLanguage'] = originalLang
                        item['hasOriginalTitle'] = originalTitle
                        item['hasOverview'] = overview
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'isAdult' : adult,
                        'partOfCollections' : collectionDataList,
                        'hasBudget' : budget,
                        'ofGenre' : genresList,
                        'hasOriginalLanguage' : originalLang,
                        'hasOriginalTitle' : originalTitle,
                        'hasOverview' : overview
                    }
                    jsonMovieData.append(movie_data)
            print("Duplicate MetaData Count : ", duplicateOverwrites)
            print("MetaData Entries read : ",metaDataCount)
            logging.info(f"MetaData count : {metaDataCount}")

    except FileNotFoundError:
        logging.error(f"MetaData error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"MetaData error : {e}")
        print(f"An error occurred: {e}")

def readRatings(filePath:str):
    try:
        with open(filePath, mode='r', encoding='utf-8') as file:
            logging.info("Ratings file opened....")
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            print("Ratings Read with headers : ",headers)
            logging.info(f"Ratings headers : {headers}")
            ratingsCount = 0
            for row in tqdm(csv_reader, desc="Reading Ratings"):
                ratingsCount = ratingsCount+1
                userId = row[0]
                _id = row[1]
                rating = row[2]
                timeStamp = row[3]
                foundFlag = False
                for item in jsonMovieData:
                    if (item['_id']==_id) and ('hasRating' in item.keys()):
                        foundFlag = True
                        temp_rating = item['rating']
                        temp_rating.append(rating)
                        item['hasRating'] = temp_rating
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        'hasRating' : [rating]
                    }
                    jsonMovieData.append(movie_data)
            print("Rating Entries read : ",ratingsCount)
            logging.info(f"Ratings count : {ratingsCount}")

    except FileNotFoundError:
        logging.error(f"Ratings error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"Ratings error : {e}")
        print(f"An error occurred: {e}")

def printSampleJsonData(printType:str):
    sampleData = jsonMovieData[0]
    if printType=='value':
        print("\nSample Data : ", end=None)
        print(json.dumps(sampleData,indent=4))
        logging.info(f"Sample Data : {json.dumps(sampleData, indent=4)}")
    else:
        typesData = {}
        keys = list(sampleData.keys())
        for key in keys:
            typesData[key] = str(type(sampleData[key]))
        print("Data Types : ", end=None)
        print(json.dumps(typesData, indent=4), end="\n\n")
        logging.info(f"Data Types : {json.dumps(typesData, indent=4)}")

# Functions to process JSON data and simplify parameters

def processCredits():
    newJsonData = []
    logging.info("Begin Credits Processing....")
    for item in tqdm(jsonMovieData, desc="Processing Credits Data...."):
        if 'castList' in item.keys():
            castList = []
            if isinstance(item['castList'],str):
                castList = json.loads(str(item['castList']).replace("'",'"'))
            else:
                castList = item['castList']
            castFin = []
            for cast in castList:
                actor = str(cast['name'])
                if actor not in castFin:
                    castFin.append(actor)
            item['actedBy'] = castFin
            item = item.pop('castList')
        if 'crewList' in item.keys():
            crewList = []
            if isinstance(item['crewList'],str):
                crewList = json.dumps(str(item['crewList']).replace("'",'"'))
            else:
                crewList = item['crewList']
            # Multiple types of Crews available
            directors = []
            writers = []
            producers = []
            artists = []
            editors = []
            sounds = []
            visualEffects = []
            lighting = []
            supportCrew = []
            for crew in crewList:
                name = str(crew['name'])
                department = str(crew['department']).strip()         # Directing, Writing, Production, Art, Editing, Sound, Visual Effects, Crew, Lighting, ' '
                if department=='Directing':
                    if name not in directors:
                        directors.append(name)
                elif department=='Writing':
                    if name not in writers:
                        writers.append(name)
                elif department=='Production':
                    if name not in producers:
                        producers.append(name)
                elif department=='Art':
                    if name not in artists:
                        artists.append(name)
                elif department=='Editing':
                    if name not in editors:
                        editors.append(name)
                elif department=='Sound':
                    if name not in sounds:
                        sounds.append(name)
                elif department=='Visual Effects':
                    if name not in visualEffects:
                        visualEffects.append(name)
                elif department=='Lighting':
                    if name not in lighting:
                        lighting.append(name)
                else:
                    if name not in supportCrew:
                        supportCrew.appen(name)
            item['directedBy'] = directors
            item['writtenBy'] = writers
            item['producedBy'] = producers
            item['supportingArtists'] = artists
            item['editedBy'] = editors
            item['soundsBy'] = sounds
            item['visualEffectsBy'] = visualEffects
            item['lightingBy'] = lighting
            item.pop('crewList')
        newJsonData.append(item)
    print(f"Old ({len(jsonMovieData)}) -> Processed ({len(newJsonData)})")
    logging.info("Complete Credits Processing....")
    logging.info(f"Dropped {len(jsonMovieData)-len(newJsonData)} Items....")
    jsonMovieData = newJsonData
    printSampleJsonData(printType='dataType')

def processRatings():
    newJsonData = []
    logging.info("Begin Ratings Processing....")
    for item in tqdm(jsonMovieData, desc="Processing Ratings Data...."):
        avg_rating = 0.0
        ratings = item['hasRating']
        if len(ratings>0):
            for value in ratings:
                avg_rating = avg_rating+value
            avg_rating = avg_rating/len(ratings)
        item['hasAverageRating'] = round(avg_rating, ndigits=2)
        newJsonData.append(item)
    logging.info("Complete Ratings Processing....")
    logging.info(f"Dropped {len(jsonMovieData)-len(newJsonData)} Items")
    jsonMovieData = newJsonData

# Function to Write JSON data to JSON file for temporary storage

def writeToJson(outputFile: str):
    try:
        with open(outputFile, mode='w', encoding='utf-8') as file:
            json.dump(jsonMovieData, file, indent=4, ensure_ascii=False)
        logging.info("Written to JSON File....")
        print(f"JSON data has been written to {outputFile}")

    except TypeError as e:
        logging.error(f"Trying to write to JSON file : {e}")
        print(f"Error: Provided data is not JSON serializable. {e}")
    except Exception as e:
        logging.error(f"Trying to write to JSON file : {e}")
        print(f"An error occurred while writing to the file: {e}")

# Function to iterate through each downloaded file in cache folder and invoke relevant functions

def list_files_in_folder(folder_path):
    file_names = []
    if not os.path.exists(folder_path):
        logging.warning(f"Trying to open invalid folder {folder_path}")
        print(f"The folder '{folder_path}' does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file not in ('ratings_small.csv', 'links_small.csv'):
                file_names.append(file)
                filePath = os.path.join(root,file)
                if 'credits.csv' in file:
                    logging.info("Reading Credits")
                    readCredits(filePath=filePath)
                    logging.info("Reading Credits Completed")
                    processCredits()
                elif 'keywords.csv' in file:
                    logging.info("Reading Keywords")
                    readKeyWords(filePath=filePath)
                    logging.info("Reading Keywords Completed")
                elif 'links.csv' in file:
                    logging.info("Reading Links")
                    readLinks(filePath=filePath)
                    logging.info("Reading Links Completed")
                elif 'movies_metadata.csv' in file:
                    logging.info("Reading MetaData")
                    readMetaData(filePath=filePath)
                    logging.info("Reading MetaData Completed")
                elif 'ratings.csv' in file:
                    # print("Ratings Pending")
                    logging.info("Reading Ratings")
                    readRatings(filePath=filePath)
                    logging.info("Reading Ratings Completed")
                    processRatings()
                print("Current Json Structure : ", end=None)
                printSampleJsonData('types')
                calculateTotalTime("final")
    print("Unified Data Count : ",len(jsonMovieData))
    printSampleJsonData('types')
    output_file_path = os.path.join(output_folder,"JsonData.json")
    writeToJson(outputFile=output_file_path)
    print("\nFiles Processed : ", file_names)     

# Calculate and display statistics of conversion

def calculateTotalTime(typeFlag:str):  
    endTime = datetime.now()
    delta = endTime-startTime
    min_delta = round(delta.total_seconds()/60)
    sec_delta = round(delta.total_seconds() - (min_delta*60), ndigits=3)
    hour_delta = round(min_delta/60)
    if typeFlag=="final":
        logging.info("Calculating Total Elapsed Time....")
        print("\nTotal Conversion Duration : ", end=None)
    else:
        logging.info("Calculating Current Elapsed Time....")
        print("\nTime Elapsed : ", end=None)
    if hour_delta>0:
        min_delta = min_delta-(hour_delta*60)
        print(hour_delta," hours, ", end=None)
    logging.info(f"Elapsed Time : {hour_delta} hours, {min_delta} minutes, {sec_delta} seconds")
    print(min_delta," minutes and ",sec_delta," seconds")  

def main():
    logging.info("Program started....")
    # Get Files from Kaggle
    path = kagglehub.dataset_download(kaggle_dataset)
    logging.info("Dataset Downloaded....\n")
    print("Path to dataset temporary files:", path)

    list_files_in_folder(path)
    calculateTotalTime("final")

if __name__=="__main__":
    log_file = "./outputLogs/converterLogs.txt"
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,  # Set logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )
    main()
    logging.info("Program finished....")