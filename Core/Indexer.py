#!/usr/bin/python
# -*- coding=utf-8 -*-
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
        for doc, items in docs.items():
            data[doc] = Indexer.indexDoc(items, stopWords)
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
