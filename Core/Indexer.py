#!/usr/bin/python
# -*- coding=utf-8 -*-
import math
from collections import Counter
from .Tokenizer import Tokenizer

class Indexer:
    @staticmethod
    def indexDoc(doc, stopWords):
        tokens = Tokenizer.tokenize(doc, stopWords)
        vocab = Tokenizer.defineVocabulary(tokens)
        return dict(vocab)

    @staticmethod
    def indexDocs(docs, stopWords):
        data = dict()
        data['length'] = dict()
        data['freq'] = dict()
        for doc, items in docs.items():
            data['length'][doc] = len(items)
            data['freq'][doc] = Indexer.indexDoc(items, stopWords)
        return data

    @staticmethod
    def mergedIndexes(indexes):
        # getting a list of all the terms
        c = Counter()
        for index in indexes.keys():
            c.update(list(indexes[index].keys()))
        # creating a dict that contains all the terms and their frequency in the docs
        data = dict()
        for term in c.keys():
            data[term] = dict()
            # for index in indexes.keys():
            #     data[term][index] = 0
        # updating the frequency
        for index, freqs in indexes.items():
            for term, freq in freqs.items():
                data[term][index] = freq
        return data

    @staticmethod
    def weightIndexes(mergedIndexes, lengths):
        index = dict()
        for term, occurrences in mergedIndexes.items():
            index[term] = dict()
            for doc, occurrence in occurrences.items():
                # a = occurrence
                # b = lengths[doc]
                tf = occurrence / lengths[doc]
                # c = len(occurrences.keys())
                # d = len(lengths)
                idf = math.log( (len(occurrences.keys()) / len(lengths)) + 1)
                index[term][doc] = tf*idf
        return index