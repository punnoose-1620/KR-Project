# To run data converter with runtime logs, use the command given below
# python .\data_converter.py > .\outputLogs\converterOutput.txt
import os
import csv
import json
import logging
import kagglehub
from tqdm import tqdm
from constants import *
from datetime import datetime
from rdflib import Graph, URIRef, Literal, Namespace

jsonMovieData = []
additionalMovieYearData = {}
additionalMoviePosterData = {}
startTime = datetime.now()
endTime = datetime.now()
dataLimit = 150

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
                        item[keywordsKey] = keywords
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        keywordsKey : keywords
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
                        item[imdbIdKey] = imdbId
                        item[tmdbIdKey] = tmdbId
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        imdbIdKey : imdbId,
                        tmdbIdKey : tmdbId
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
                posterPath = row[11]
                foundFlag = False
                for item in jsonMovieData:
                    if item['_id']==_id:
                        foundFlag = True
                        if adultKey in item.keys():
                            duplicateOverwrites = duplicateOverwrites+1
                        item[adultKey] = adult
                        item[collectionsKey] = collectionDataList
                        item[budgetKey] = budget
                        item[genreKey] = genresList
                        item[languageKey] = originalLang
                        item[titleKey] = originalTitle
                        item[overviewKey] = overview
                        item[posterKey] = posterPath
                if foundFlag==False:
                    movie_data = {
                        '_id' : _id,
                        adultKey : adult,
                        collectionsKey : collectionDataList,
                        budgetKey : budget,
                        genreKey : genresList,
                        languageKey : originalLang,
                        titleKey : originalTitle,
                        overviewKey : overview,
                        posterKey: posterPath
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
            ratingsObject = {}
            for row in tqdm(csv_reader, desc="Reading Ratings"):
                ratingsKeys = ratingsObject.keys()
                ratingsCount = ratingsCount+1
                userId = row[0]
                _id = row[1]
                rating = row[2]
                timeStamp = row[3]
                foundFlag = False
                if _id not in ratingsKeys:
                    ratingsObject[_id] = [rating]
                else:
                    ratingsObject[_id].append(rating)
            logging.debug("Ratings object created with rating data based on ID....")
            # Add rating from ratingsObject to jsonMovieData
            for item in jsonMovieData:
                movieId = item['_id']
                if movieId in ratingsObject.keys():
                    rats = ratingsObject[movieId]
                    item[ratingsKeys] = rats
                    ratingsObject.pop(movieId)
            logging.debug("Ratings added to movie data....")
            print("Rating Entries read : ",ratingsCount)
            logging.info(f"Ratings count : {ratingsCount}")

    except FileNotFoundError:
        logging.error(f"Ratings error : {e}")
        print(f"The file '{filePath}' does not exist.")
    except Exception as e:
        logging.error(f"Ratings error : {e}")
        print(f"An error occurred: {e}")

def checkMissingKeys(key:str):
    count = 0
    for item in jsonMovieData:
        if key not in item.keys():
            count = count+1
    print(f"{count} items without {key}")
    logging.warning(f"{count} items found in movies without the key {key}")

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

def getCastNames(stringVal:str):
    names = []
    splitByKey = stringVal.split("'name': '")[1:]
    for item in splitByKey:
        splitByQuote = item.split("'")
        names.append(splitByQuote[0])
    return names

def getCrewNames(StringVal:str):
    names = []
    departments = []
    categorisation = {
        directorKey: [],
        writerKey: [],
        producerKey: [],
        supportingArtistKey: [],
        editorKey: [],
        soundsKey: [],
        visualEffectsKey: [],
        lightingKey: []
    }
    splitByDept = StringVal.split("'department':")[1:]
    splitByName = StringVal.split("'name':")[1:]
    length = len(splitByDept)
    if len(splitByDept)==len(splitByName):
        for i in range(length):
            deptPre = splitByDept[i]
            namePre = splitByName[i]
            if deptPre[0]=="'":
                departments.append("Empty")
            else:
                deptPost = deptPre.split("',")[0].replace("'","").strip()
                departments.append(deptPost)
            if namePre[0]=="'":
                names.append("Empty")
            else:
                namePost = namePre.split("',")[0].replace("'","").strip()
                names.append(namePost)
    if len(departments)==len(names):
        for i in range(len(departments)):
            dept = departments[i]
            name = names[i]
            if 'Empty' not in name:
                if dept=='Directing':
                    if name not in categorisation[directorKey]:
                        categorisation[directorKey].append(name)
                elif dept=='Writing':
                    if name not in categorisation[writerKey]:
                        categorisation[writerKey].append(name)
                elif dept=='Production':
                    if name not in categorisation[producerKey]:
                        categorisation[producerKey].append(name)
                elif dept=='Art':
                    if name not in categorisation[supportingArtistKey]:
                        categorisation[supportingArtistKey].append(name)
                elif dept=='Editing':
                    if name not in categorisation[editorKey]:
                        categorisation[editorKey].append(name)
                elif dept=='Sound':
                    if name not in categorisation[soundsKey]:
                        categorisation[soundsKey].append(name)
                elif dept=='Visual Effects':
                    if name not in categorisation[visualEffectsKey]:
                        categorisation[visualEffectsKey].append(name)
                elif dept=='Lighting':
                    if name not in categorisation[lightingKey]:
                        categorisation[lightingKey].append(name)
                else:
                    if name not in categorisation[supportingArtistKey]:
                        categorisation[supportingArtistKey].append(name)
    return categorisation

def processCredits():
    newJsonData = []
    castFin = []
    global jsonMovieData
    logging.info("Begin Credits Processing....")
    checkMissingKeys('castList')
    checkMissingKeys('crewList')
    for item in tqdm(jsonMovieData, desc="Processing Credits Data...."):
        if 'castList' in item.keys():
            castList = []
            if isinstance(item['castList'],str):
                castFin = getCastNames(item['castList'])
            else:
                castList = item['castList']
            for cast in castList:
                if isinstance(cast, str):
                    logging.debug(f"Cast item : {cast}")
                actor = str(cast['name'])
                if actor not in castFin:
                    castFin.append(actor)
            item[actorKey] = castFin
            item.pop('castList')
        if 'crewList' in item.keys():
            crewList = []
            crewData = {}
            if isinstance(item['crewList'],str):
                crewData = getCrewNames(item['crewList'])
            else:
                crewList = item['crewList']
            # Multiple types of Crews available
            if len(crewList)>0:
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
                item[directorKey] = directors
                item[writerKey] = writers
                item[producerKey] = producers
                item[supportingArtistKey] = artists
                item[editorKey] = editors
                item[soundsKey] = sounds
                item[visualEffectsKey] = visualEffects
                item[lightingKey] = lighting
            else:
                for key in crewData.keys():
                    item[key] = crewData[key]
            item.pop('crewList')
        newJsonData.append(item)
    print(f"Old ({len(jsonMovieData)}) -> Processed ({len(newJsonData)})")
    logging.info("Complete Credits Processing....")
    logging.info(f"Dropped {len(jsonMovieData)-len(newJsonData)} Items....")
    jsonMovieData = newJsonData
    printSampleJsonData(printType='dataType')

def processRatings():
    newJsonData = []
    global jsonMovieData
    logging.info("Begin Ratings Processing....")
    checkMissingKeys('hasRating')
    for item in tqdm(jsonMovieData, desc="Processing Ratings Data...."):
        avg_rating = 0.0
        if 'hasRating' in item.keys():
            ratings = item['hasRating']
            if len(ratings)>0:
                for value in ratings:
                    avg_rating = avg_rating+float(value)
                avg_rating = avg_rating/len(ratings)
            item[averateRatingKey] = round(avg_rating, ndigits=2)
            item.pop('hasRating')
        newJsonData.append(item)
    logging.info("Complete Ratings Processing....")
    logging.info(f"Dropped {len(jsonMovieData)-len(newJsonData)} Items")
    checkMissingKeys(averateRatingKey)
    jsonMovieData = newJsonData

# Function to drop entries that do not have the given key

def dropEntries(key: str):
    global jsonMovieData
    initialLength = len(jsonMovieData)
    newMoviesList = []
    for movie in tqdm(jsonMovieData, desc="Dropping Keys...."):
        if key in movie.keys():
            if 'poster' in key.strip().lower():
                if 'http' in movie[key]:
                    newMoviesList.append(movie)
            else:
                if str(movie[key]).strip()!='':
                    newMoviesList.append(movie)
    finalLength = len(newMoviesList)
    print(f"{finalLength-initialLength} Entries Dropped based on {key}")
    jsonMovieData = newMoviesList

# Function to Write JSON data to JSON file for temporary storage

def writeToJson(outputFile: str):
    try:
        with open(outputFile, mode='w', encoding='utf-8') as file:
            json.dump(jsonMovieData[:dataLimit], file, indent=4, ensure_ascii=False)
        logging.info("Written to JSON File....")
        print(f"JSON data has been written to {outputFile}")

    except TypeError as e:
        logging.error(f"Trying to write to JSON file : {e}")
        print(f"Error: Provided data is not JSON serializable. {e}")
    except Exception as e:
        logging.error(f"Trying to write to JSON file : {e}")
        print(f"An error occurred while writing to the file: {e}")

# Function to write Processed JSON data to RDF Database

def writeToRdf(outputFile: str):
    logging.info("Begin Creating RDF Graph....")
    # Create an RDF graph
    graph = Graph()
    temp = {}
    # Define a namespace for the properties
    ns = Namespace(sampleNameSpace)
    for item in tqdm(jsonMovieData[:dataLimit], desc="Writing Data to RDF File...."):
        # Create a unique URI for each individual using the "_id"
        subject = URIRef(subjectRefUri+str(item['_id']))

        for key,value in item.items():
            if value=="Empty":
                value = ""
            predicate = ns[key]         # Using Key as Property Name
            obj = Literal('')           # Create a Dummy value
            if isinstance(value,list):
                for listItem in value:
                    graph.add((subject, predicate, Literal(listItem)))
                continue
            else:
                obj = Literal(value)
            graph.add((subject, predicate, obj))
    logging.info("RDF Graph Created....")
    logging.info("Begin Writing to RDF File....")
    graph.serialize(destination=outputFile, format='turtle')
    print(f"RDF data has been written to {outputFile}")
    logging.info("Completed Writing to RDF File....")

# Write data to a page for referring sample data

def writeSampleData(outputFile: str):
    if len(jsonMovieData)>0:
        refKeys = []
        for item in jsonMovieData:
            jsonKeys = item.keys()
            for keytemp in jsonKeys:
                if keytemp not in refKeys:
                    refKeys.append(keytemp)
        sampleDataObject = {}
        for key in tqdm(refKeys, desc='Writing Sample Data....'):
            tempArr = []
            for movie in jsonMovieData[:101]:
                if key in movie:
                    movieItem = movie[key]
                    if isinstance(movieItem,list):
                        for t_item in movieItem:
                            if t_item not in tempArr:
                                tempArr.append(t_item)
                    elif movieItem not in tempArr:
                        tempArr.append(movieItem)
                sampleDataObject[key] = tempArr
        try:
            with open(outputFile, mode='w', encoding='utf-8') as file:
                json.dump(sampleDataObject, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Sample Data Error: Provided data is not JSON serializable. {e}")

# Function to iterate through each downloaded file in cache folder and invoke relevant functions

def list_files_in_folder(folder_path):
    file_names = []
    global jsonMovieData
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
                    logging.info("Reading Ratings")
                    readRatings(filePath=filePath)
                    logging.info("Reading Ratings Completed")
                    processRatings()
                print("Current Json Structure : ", end=None)
                printSampleJsonData('types')
        calculateTotalTime("final")
    print("Unified Data Count : ",len(jsonMovieData))
    print("Final Data Count Taken : ",len(jsonMovieData[:101]))
    printSampleJsonData('types')
    checkMissingKeys('hasKeywords')
    dropEntries(titleKey)

    getAdditionalYearData()
    print("Additional Year Data Count : ", len(additionalMovieYearData.keys()))
    getAdditionalPosterData()
    print("Additional Poster Data Count : ", len(additionalMoviePosterData.keys()))
    year_match_count = 0
    poster_match_count = 0
    for movie in tqdm(jsonMovieData, desc="Getting Release Year for movies...."):
        if titleKey in movie.keys():
            title = str(movie[titleKey]).lower().strip()
            if title in additionalMovieYearData.keys():
                year_match_count = year_match_count+1
                movie[releaseYearKey] = additionalMovieYearData[title]
            if title in additionalMoviePosterData.keys():
                poster_match_count = poster_match_count+1
                movie[posterKey] = additionalMoviePosterData[title]
    print(f"\n{year_match_count} years updated, {poster_match_count} posters updated")
    dropEntries(releaseYearKey)
    dropEntries(posterKey)

    output_file_path = os.path.join(dataConverterOutputFolder,dataConverterOutputRdf)
    outputJsonFilePath = os.path.join(dataConverterOutputFolder,dataConverterOutputJson)
    outputSampleJsonFilePath = os.path.join(dataConverterOutputFolder,sampleDataFile)
    writeToJson(outputJsonFilePath)
    writeToRdf(output_file_path)
    writeSampleData(outputSampleJsonFilePath)
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

def getAdditionalYearData():
    dataPath = kagglehub.dataset_download(secondaryDataset)
    # Read from this set and update to jsonMovieData
    filePath = ""
    for root, _, files in os.walk(dataPath):
        for file in files:
            filePath = os.path.join(root,file)
            try:
                with open(filePath, mode='r', encoding='utf-8') as f:
                    csv_reader = csv.reader(f)
                    headers = next(csv_reader, None)
                    print("Additional Data for Year Read with headers : ",headers)
                    for row in tqdm(csv_reader, desc="Reading Secondary Data...."):
                    # for row in csv_reader:
                        title = str(row[1]).lower().strip()
                        releaseDate = str(row[5]).strip()
                        if len(releaseDate)>0 and ('-' in releaseDate):
                            releaseYear = releaseDate.split('-')[0]
                            if title not in additionalMovieYearData.keys():
                                additionalMovieYearData[title] = releaseYear
            except FileNotFoundError:
                print(f"The file '{filePath}' does not exist.")
            except Exception as e:
                logging.error(f"Credits error : {e}")
                print(f"An error occurred: {e}")

def getAdditionalPosterData():
    dataPath = kagglehub.dataset_download(tertiaryDataset)
    # Read from this set and update to jsonMovieData
    filePath = ""
    for root, _, files in os.walk(dataPath):
        for file in files:
            filePath = os.path.join(root,file)
            # print(f"Poster File : {file}, FilePath : {filePath}")
            try:
                with open(filePath, mode='r', encoding='utf-8') as f:
                    csv_reader = csv.reader(f)
                    headers = next(csv_reader, None)
                    print("Additional Data for Posters Read with headers : ",headers)
                    for row in tqdm(csv_reader, desc="Reading Secondary Data...."):
                        poster = str(row[0])
                        title = str(row[1]).lower().strip()
                        releaseYear = str(row[2])
                        if title not in additionalMovieYearData.keys():
                            additionalMovieYearData[title] = releaseYear
                        if title not in additionalMoviePosterData.keys():
                            additionalMoviePosterData[title] = poster
            except FileNotFoundError:
                print(f"The file '{filePath}' does not exist.")
            except Exception as e:
                logging.error(f"Credits error : {e}")
                print(f"An error occurred: {e}")

def main():
    logging.info("Program started....")
    # Get Files from Kaggle
    path = kagglehub.dataset_download(kaggleDataset)
    logging.info("Dataset Downloaded....\n")
    print("Path to dataset temporary files:", path)

    list_files_in_folder(path)
    calculateTotalTime("final")

if __name__=="__main__":
    logging.basicConfig(
        filename=dataConverterLog,
        level=logging.DEBUG,  # Set logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )
    main()
    logging.info("Program finished....")