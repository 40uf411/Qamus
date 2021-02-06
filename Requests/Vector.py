#!/usr/bin/python
# -*- coding=utf-8 -*-
import sys
sys.path.append("..")
from Core.Tokenizer import Tokenizer

class VectorRequest():
    
    def __init__(self, query, stopWords=[]):
        self.query = query
        self.tokens = dict()
        self.tokens['occurrences'] = dict()
        self.tokens['frequency'] = dict()
        self.tokens = self.parse(Tokenizer.tokenize(query, stopWords))

    def parse(self, tokens):
        data = dict()
        data['occurrences'] = dict()
        data['frequency'] = dict()
        
        for token in tokens:
            if token not in data['occurrences'].keys():
                data['occurrences'][token] = 1
                data['frequency'][token] = 1/len(tokens)
            else:
                data['occurrences'][token] += 1 
                data['frequency'][token] = data['occurrences'][token] / len(tokens)
        
        return data