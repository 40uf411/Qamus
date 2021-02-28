#!/usr/bin/python
# -*- coding=utf-8 -*-
import math
from operator import itemgetter

class VectorModule():
    INNER_PRODUCT_SIMILARITY = 0
    DICE_COEFFICIENT_SIMILARITY = 1
    COSINUS_SIMILARITY = 2
    JACCARD_INDEX_SIMILARITY = 3
    DEFAULT_SIMILARITY = INNER_PRODUCT_SIMILARITY

    @staticmethod
    def validSimilarityMethod(method):
        if method in [
                        VectorModule.INNER_PRODUCT_SIMILARITY, VectorModule.DICE_COEFFICIENT_SIMILARITY, 
                        VectorModule.COSINUS_SIMILARITY, VectorModule.JACCARD_INDEX_SIMILARITY
                    ]:
            return True

    @staticmethod
    def defaultSimilarity(method):
        if VectorModule.validSimilarityMethod(method):
            VectorModule.DEFAULT_SIMILARITY = method

    @staticmethod
    def search(request, index, options={}):
        method = options['similarityMethod'] \
                if ('similarityMethod' in options.keys() and VectorModule.validSimilarityMethod(options['similarityMethod'])) \
                else VectorModule.DEFAULT_SIMILARITY
        result = dict()
        if method == VectorModule.INNER_PRODUCT_SIMILARITY:
            result = VectorModule.innerProductSimilarity(request.tokens['frequency'], index)
        if method == VectorModule.DICE_COEFFICIENT_SIMILARITY:
            result = VectorModule.diceCoefficientSimilarity(request.tokens['frequency'], index)
        if method == VectorModule.COSINUS_SIMILARITY:
            result = VectorModule.cosinustSimilarity(request.tokens['frequency'], index)
        else:
            result = VectorModule.jaccardIndexSimilarity(request.tokens['frequency'], index)
            
        result = sorted(result.items(), key=itemgetter(1), reverse=True)
        if 'minRel' in options.keys():
            tmp = list()
            for elem in result:
                if elem[1] >= options['minRel']:
                    tmp.append(elem)
                else:
                    break;
            result = tmp
        if 'dict' in options.keys() and options['dict'] == True:
            return dict(result)
        else:
            return result

    @staticmethod
    def innerProductSimilarity(query, index):
        result = dict()
        for term, freq in query.items():
            try:
                for doc, tfidf in index[term].items():
                    try:
                        result[doc] = result[doc] + (freq * tfidf)
                    except:
                        result[doc] =  (freq * tfidf)
            except: # if a term in request does not exist in the index
                continue
        return result

    @staticmethod
    def diceCoefficientSimilarity(query, index):
        ips = VectorModule.innerProductSimilarity(query, index)
        top = dict()
        for key, val in ips.items():
            top[key] = val * 2
        # Calculate the bottom
        sumXSquare = sum([(elem**2) for elem in query.values()])
        sumYSquare = dict()
        for term in query.keys():
            try:
                for doc, freq in index[term].items():
                    try:
                        sumYSquare[doc] = sumYSquare[doc] + (freq ** 2)
                    except:
                        sumYSquare[doc] = (freq ** 2)
            except: # if a term in request does not exist in the index
                continue
        bottom = dict()
        for doc in sumYSquare.keys():
            bottom[doc] = sumXSquare + sumYSquare[doc]
        result = dict()
        for key, val in top.items():
            result[key] = val / bottom[key]
        return result

    @staticmethod
    def cosinustSimilarity(query, index):
        top = VectorModule.innerProductSimilarity(query, index)
        # Calculate the bottom
        sumXSquare = sum([(elem**2) for elem in query.values()])
        sumYSquare = dict()
        for term in query.keys():
            try:
                for doc, freq in index[term].items():
                    try:
                        sumYSquare[doc] = sumYSquare[doc] + (freq ** 2)
                    except:
                        sumYSquare[doc] = (freq ** 2)
            except: # if a term in request does not exist in the index
                continue
        bottom = dict()
        for doc in sumYSquare.keys():
            bottom[doc] = math.sqrt(sumXSquare + sumYSquare[doc])
        result = dict()
        for key, val in top.items():
            result[key] = val / bottom[key]
        return result

    @staticmethod
    def jaccardIndexSimilarity(query, index):
        top = VectorModule.innerProductSimilarity(query, index)
        # Calculate the bottom
        sumXSquare = sum([(elem**2) for elem in query.values()])
        sumYSquare = dict()
        for term in query.keys():
            try:
                for doc, freq in index[term].items():
                    try:
                        sumYSquare[doc] = sumYSquare[doc] + (freq ** 2)
                    except:
                        sumYSquare[doc] = (freq ** 2)
            except: # if a term in request does not exist in the index
                continue
        bottom = dict()
        for doc in sumYSquare.keys():
            bottom[doc] = sumXSquare + sumYSquare[doc]
        result = dict()
        for key, val in top.items():
            result[key] = val / (bottom[key]-val)
        return result