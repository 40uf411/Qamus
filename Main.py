from Qamus.Core.FilesLoader import FileLoader
from Qamus.Core.Tokenizer import Tokenizer
from Qamus.Core.Indexer import Indexer
from Qamus.Core.SearchEngine import SearchEngine
from Qamus.Core.Evaluator import Evaluator

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Config %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
DOCS_DIR = '/media/zsasz/Ali1/study/2021/ri/tpri/docs/'
DOCS_ENCODING = 'ISO-8859-1'
DOCS = [
    # DOCS_DIR + 'D0.txt',
    # DOCS_DIR + 'D1.txt',
    # DOCS_DIR + 'D2.txt',
    DOCS_DIR + 'D3.txt',
    # DOCS_DIR + 'D4.txt',
    # DOCS_DIR + 'D5.txt',
    DOCS_DIR + 'D6.txt',
    # DOCS_DIR + 'D7.txt',
    # DOCS_DIR + 'D8.txt',
    DOCS_DIR + 'D9.txt',
    # DOCS_DIR + 'D10.txt',
    # DOCS_DIR + 'D11.txt',
    DOCS_DIR + 'D12.txt',
    # DOCS_DIR + 'D13.txt',
    # DOCS_DIR + 'D14.txt',
]
STOPWORDS_FILE = '/media/zsasz/Ali1/study/2021/ri/tpri/docs/stopwords_fr.txt'
STOPWORDS_ENCODING = 'utf-8'
INCLUDE_IDF = True
IDF_METHOD = SearchEngine.IDF_METHOD_DIV # SearchEngine.IDF_METHOD_DIV | SearchEngine.IDF_METHOD_LOG

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Code %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
from Qamus.Datasets.CACM.Api import Loader
data = Loader.loadData()
corpus = Loader.corpus('T', 'W', 'A')

# ? Create a search engine from a group of docs
# initialize the search engine
# SearchEngine.init(
#     corpusFiles=DOCS, 
#     stopwordsFile=STOPWORDS_FILE, 
#     docs_encoding=DOCS_ENCODING, 
#     stopwords_encoding=STOPWORDS_ENCODING
#     )
# index = SearchEngine.docTerms('/media/zsasz/Ali1/study/2021/ri/tpri/docs/D3.txt')
# term = SearchEngine.termFeq('1963')

# ? Create a search engine using a dataset
# initialize the search engine
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

SearchEngine.init(
    dataset=corpus, 
    stopwords=stopwords.words('english')
    )
print()
# index = SearchEngine.docIndexes()
# term = SearchEngine.termFeq('computer')

# ? testing the boolean request
#result = SearchEngine.search('algebraic and set', model=SearchEngine.BOOLEAN_MODEL)
ev = Loader.evaluation
# result = SearchEngine.search(
#     request=ev[i]['query']['W'], 
#     model=SearchEngine.VECTOR_MODEL, 
#     options = {
#         'similarityMethod': SearchEngine.JACCARD_INDEX_SIMILARITY, 
#         'dict': True, 
#         'minRel': 0.0001
#     })
result = SearchEngine.search(
    request='( science or compiler ) and not algebra and code', 
    model=SearchEngine.VECTOR_MODEL, 
    options = {
        'similarityMethod': SearchEngine.JACCARD_INDEX_SIMILARITY, 
        'dict': True, 
        'minRel': 0.0001
    })
e = Loader.evaluationQueries(keys=['W'], seperat=True)

Evaluator.init(
    queries=e['queries'],
    results=e['results'],
    minRel=1e-3
)
fs = Evaluator.accuracy()
print(list(result.items())[:3])
# load an existing model
# SearchEngine.load(fileName='engineNoData.json', encoding=DOCS_ENCODING)
print()
# save index
#SearchEngine.save('engineWithData.json', saveData=True)

# %%
