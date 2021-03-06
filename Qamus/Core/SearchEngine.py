#!/usr/bin/python
# -*- coding=utf-8 -*-
import math
import time
import json

from .FilesLoader import FileLoader
from .Tokenizer import Tokenizer
from .Indexer import Indexer

from ..Models.Boolean import BooleanModule
from ..Requests.Boolean import BooleanRequest
from ..Models.Vector import VectorModule
from ..Requests.Vector import VectorRequest

class SearchEngine:
    BOOLEAN_MODEL = 0
    VECTOR_MODEL = 1

    INNER_PRODUCT_SIMILARITY = VectorModule.INNER_PRODUCT_SIMILARITY
    DICE_COEFFICIENT_SIMILARITY = VectorModule.DICE_COEFFICIENT_SIMILARITY
    COSINUS_SIMILARITY = VectorModule.COSINUS_SIMILARITY
    JACCARD_INDEX_SIMILARITY = VectorModule.JACCARD_INDEX_SIMILARITY

    IDF_METHOD_DIV = 0
    IDF_METHOD_LOG = 1

    index = None
    __init = False

    @staticmethod
    def init(corpusFiles='', stopwordsFile='', dataset={}, stopwords=[], docs_encoding='utf-8', stopwords_encoding='utf-8'):
        if corpusFiles != '':
            # save the corpus
            SearchEngine.__corpus = corpusFiles 
            # loading the documents
            SearchEngine.__data = FileLoader.readFiles(filesNames=corpusFiles, encoding=docs_encoding)
        else:
            # save the corpus
            SearchEngine.__corpus = list(dataset.keys())
            # loading the documents
            SearchEngine.__data = dataset
        
        if stopwordsFile != '':
            # loading stop words
            SearchEngine.__stopWords = FileLoader.loadStopWords(fileName=stopwordsFile, encoding=stopwords_encoding)
        else:
            # loading stop words
            SearchEngine.__stopWords = stopwords
        # indexing documents
        SearchEngine.__indexes = Indexer.indexDocs(docs=SearchEngine.__data, stopWords=SearchEngine.__stopWords)
        # merging indexes
        SearchEngine.__mergedIndexes = Indexer.mergedIndexes(SearchEngine.__indexes['freq'])
        # weight the indexes
        SearchEngine.__mergedIndexes = Indexer.weightIndexes(SearchEngine.__mergedIndexes, SearchEngine.__indexes['length'])
        # covert data into a list
        SearchEngine.__data = dict(SearchEngine.__data)
        # initiation is done!
        SearchEngine.__init = True

    @staticmethod
    def corpus():
        return SearchEngine.__corpus

    @staticmethod
    def uniqueTerms():
        return list(SearchEngine.__mergedIndexes.keys())

    @staticmethod
    def docTerms(id):
        return SearchEngine.__indexes[id] if id in SearchEngine.__indexes.keys() else dict()

    @staticmethod
    def docIndexes():
        return SearchEngine.__indexes

    @staticmethod
    def termFeq(id):
        return SearchEngine.__mergedIndexes[id] if id in SearchEngine.__mergedIndexes.keys() else dict()

    @staticmethod
    def search(request, model=0, options={}):
        if model == SearchEngine.BOOLEAN_MODEL:
            return BooleanModule.search(
                request=BooleanRequest(request),
                indexes=SearchEngine.__indexes['freq']
            )
        elif model == SearchEngine.VECTOR_MODEL:
             return VectorModule.search(
                 request=VectorRequest(request, SearchEngine.__stopWords),
                 index=SearchEngine.__mergedIndexes, 
                 options=options
             ) 

    @staticmethod
    def save(fileName):
        data = dict()
        data['data'] = SearchEngine.__data
        data['indexes'] = SearchEngine.__indexes
        data['mergedIndexes'] = SearchEngine.__mergedIndexes
        data['stopwords'] = SearchEngine.__stopWords
        with open(fileName, 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def load(fileName, encoding='utf-8'):
        with open(fileName,) as fp:
            data = json.load(fp) 
        SearchEngine.__corpus = data['corpus']
        SearchEngine.__indexes = data['index']
        SearchEngine.__mergedIndexes = data['mergedIndexes']
        SearchEngine.__stopWords = data['stopwords']
        # initiation is done!
        SearchEngine.__init = True

    # %% 
    # ? will be removed or used somewhere else

    @staticmethod
    def __OldPrintSearch(term, maxItems=5, minOccurrences=1, showStat=False,includeIDF=True, methodIDF=IDF_METHOD_DIV):
        print("Searching for the term '%s' in %d documents:"%(term, len(SearchEngine.__corpus)))
        start_time = time.time()
        data = SearchEngine.lookUpFor(term, minOccurrences, includeIDF, methodIDF)
        s0 = "Found %s documents  in %s seconds" % (len(list(data.keys())), time.time() - start_time)
        print(s0)
        print("="*len(s0))
        print()
        c = 1
        for doc in data.keys():
            if c > maxItems:
                break
            s = "Item %d: %s"%(c, doc) if not showStat else "Item %d: %s | TF*IDF: %d"%(c, doc, data[doc])
            print(s)
            print('-'*len(s))
            print(SearchEngine.__data[doc][:100])
            print(SearchEngine.__data[doc][100:200])
            print(SearchEngine.__data[doc][200:300])
            print()
            print()
            c += 1