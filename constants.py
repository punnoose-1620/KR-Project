# Kaggle Dataset
kaggleDataset = "rounakbanik/the-movies-dataset"
secondaryDataset = "asaniczka/tmdb-movies-dataset-2023-930k-movies"
tertiaryDataset = "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows"

# Relevant File Paths
dataConverterOutputFolder = "dataset_processed"
dataConverterLog = "./outputLogs/converterLogs.txt"
dataConverterOutputRdf = "MovieData.rdf"
dataConverterOutputJson = "MovieData.json"
queryTesterLog = "./outputLogs/queryTesterLog.txt"
endpointLog = "./outputLogs/backendLogs.txt"
sampleDataFile = "SampleData.json"

rdfFile = "./dataset_processed/MovieData.rdf"
sampleNameSpace = "http://example.org/property/"
subjectRefUri = "http://example.org/movie/"

# Keys used as Predicates
actorKey = 'actedBy'
directorKey = 'directedBy'
writerKey = 'writtenBy'
producerKey = 'producedBy'
supportingArtistKey = 'supportingArtists'
editorKey = 'editedBy'
soundsKey = 'soundsBy'
visualEffectsKey = 'visualEffectsBy'
lightingKey = 'lightingBy'
keywordsKey = 'hasKeywords'
imdbIdKey = 'imdbId'
tmdbIdKey = 'tmdbId'
adultKey = 'isAdult'
collectionsKey = 'partOfCollections'
budgetKey = 'hasBudget'
genreKey = 'ofGenre'
languageKey = 'hasOriginalLanguage'
titleKey = 'hasOriginalTitle'
overviewKey = 'hasOverview'
posterKey = 'hasPoster'
averateRatingKey = 'hasAverageRating'
releaseYearKey = 'hasReleaseYear'

# These keywors will be ignored when finding similar results
keywordsToIgnore = ['a','an','the','am','pm']

# Keys for Returning Dictionary
searchResultMovies = 'resultingMovies'
similarMovies = 'similarMovies'

# Ordering Types
ascendingOrder = 'ASC'
descendingOrder = 'DESC'
noOrder = ''

# Query Types
searchQuery = 'SEARCH'
similarQuery = 'SIMILAR'

# Person Roles
actorRole = 'ACTOR'
directorRole = 'DIRECTOR'
writerRole = 'WRITER'
producerRole = 'PRODUCER'
supportingArtistRole = 'ARTIST'
editorRole = 'EDITOR'
soundsRole = 'SOUNDS'
visualEffectsRole = 'VISUALS'
lightingRole = 'LIGHTING'
rolesList = ['ACTOR', 'DIRECTOR', 'WRITER', 'PRODUCER', 'ARTIST', 'EDITOR', 'SOUNDS', 'VISUALS', 'LIGHTING']

# search values

search_producer='Celestia'

# Values for API Endpoint
portNumber = 5000
ipAddress = "127.0.0.1"
origins = ['*', 'https://kr-project-production.up.railway.app/']

methods = ['*']

headers = ['*']

allow_credentials = True