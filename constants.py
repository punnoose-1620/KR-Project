# Kaggle Dataset
kaggleDataset = "rounakbanik/the-movies-dataset"

# Relevant File Paths
dataConverterOutputFolder = "dataset_processed"
dataConverterLog = "./outputLogs/converterLogs.txt"
dataConverterOutputRdf = "MovieData.rdf"
queryTesterLog = "./outputLogs/queryTesterLog.txt"

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
averateRatingKey = 'hasAverageRating'

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