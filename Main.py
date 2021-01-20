from FilesLoader import FileLoader
from Tokenizer import Tokenizer
from Indexer import Indexer
from SearchEngine import SearchEngine

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Config %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
DOCS_DIR = '/media/zsasz/Ali1/study/2021/ri/tpri/docs/'
DOCS_ENCODING = 'ISO-8859-1'
DOCS = [
    DOCS_DIR + 'D0.txt',
    DOCS_DIR + 'D1.txt',
    DOCS_DIR + 'D2.txt',
    DOCS_DIR + 'D3.txt',
    DOCS_DIR + 'D4.txt',
    DOCS_DIR + 'D5.txt',
    DOCS_DIR + 'D6.txt',
    DOCS_DIR + 'D7.txt',
    DOCS_DIR + 'D8.txt',
    DOCS_DIR + 'D9.txt',
    DOCS_DIR + 'D10.txt',
    DOCS_DIR + 'D11.txt',
    DOCS_DIR + 'D12.txt',
    DOCS_DIR + 'D13.txt',
    DOCS_DIR + 'D14.txt',
]
STOPWORDS_FILE = '/media/zsasz/Ali1/study/2021/ri/tpri/docs/stopwords_fr.txt'
STOPWORDS_ENCODING = 'utf-8'

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Code %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
# loading the documents
data = FileLoader.readFiles(filesNames=DOCS, encoding=DOCS_ENCODING)
# loading stop words
stopWords = FileLoader.loadStopWords(STOPWORDS_FILE, encoding=STOPWORDS_ENCODING)
# indexing documents
indexes = Indexer.indexDocs(data, stopWords)
# merging indexes
mergedIndexes = Indexer.mergedIndexes(indexes)
# initialize the search engine
SearchEngine.init(index=mergedIndexes, corpus=DOCS)
# execute a search query
searchResult = SearchEngine.lookUpFor('hommes', minOccurrences=2)
wordIDF = SearchEngine.IDF(term='hommes', fraction=False)
# DEBUG
print("Word seen in the following documents:")
print('\n - '.join(list(searchResult.keys())[:5]))
print('Word IDF: ', wordIDF)

# TODO: calculate TF*IDF
# TODO: save index