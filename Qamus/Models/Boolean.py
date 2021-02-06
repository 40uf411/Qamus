#!/usr/bin/python
# -*- coding=utf-8 -*-

class BooleanModule():

    @staticmethod
    def search(request, indexes):
        docs = list()
        for doc, index in indexes.items():
            if eval(BooleanModule.encode(request, index)):
                docs.append(doc)
        return docs
    
    @staticmethod
    def encode(request, index):
        terms = dict()
        query = ''
        for token in request.tokens:
            if len(token) == 0:
                continue
            if token in ['(', ')', 'and', 'or', 'not']:
                query = query + token + ' '
            else:
                try:
                    val = terms[token] > 0
                except:
                    try:
                        terms[token] = index[token]
                        val = terms[token] > 0
                    except:
                        terms[token] = 0
                        val = 0
                val = 1 if val > 0 else 0
                query = query + str(val) + ' '
        return query