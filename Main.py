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
INCLUDE_IDF = True
IDF_METHOD = SearchEngine.IDF_METHOD_DIV # SearchEngine.IDF_METHOD_DIV | SearchEngine.IDF_METHOD_LOG

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Code %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

# initialize the search engine
# SearchEngine.init(
#     corpus=DOCS, 
#     stopwords=STOPWORDS_FILE, 
#     docs_encoding=DOCS_ENCODING, 
#     stopwords_encoding=STOPWORDS_ENCODING
#     )

# load an existing model
# SearchEngine.load(fileName='engineNoData.json', encoding=DOCS_ENCODING)

# execute a search query
# searchResult = SearchEngine.Search(
#     term='hommes',
#     minOccurrences=2, 
#     maxItems=2,
#     showStat=True,
#     includeIDF=INCLUDE_IDF, 
#     methodIDF=IDF_METHOD
#     )

# wordIDF = SearchEngine.IDF(term='hommes', fraction=False)
# print('Word IDF: ', wordIDF)

# save index
#SearchEngine.save('engineWithData.json', saveData=True)
