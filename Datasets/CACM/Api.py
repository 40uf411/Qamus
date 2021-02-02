#!/usr/bin/python
# -*- coding=utf-8 -*-
import os 
from ..Dataset import Dataset

class Loader(Dataset):

    init = False
    data = dict()

    @staticmethod
    def loadData():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data = dict()
        with open(dir_path + '/cacm.all', 'r') as file:
            lines = file.readlines()
        
        id = ''
        key = ''
        for line in lines:
            if line[0:2] == '.I':
                id = int(line[3:].strip())
                data[id] = dict()
            elif line[0] == '.':
                key = line[1:].strip()
                data[id][key] = ''
            else:
                data[id][key] = data[id][key] + line
                
        Loader.init = True    
        Loader.data = data    
        return data
    
    @staticmethod
    def doc(id):
        if not Loader.init:
            Loader.loadData
        
        data = Loader.data[id] if (id in Loader.data.keys()) else dict()
        return data

    @staticmethod
    def value(docID, key):
        doc = Loader.doc(docID)
        return doc[key] if key in doc.keys() else ''
    
    @staticmethod
    def corpus(*attrs):
        allAttrs = True if (len(attrs) == 0) else False
        corpus = dict()
        
        for doc in Loader.data.keys():
            corpus[doc] = ''
            if allAttrs:
                for key in Loader.doc(doc).keys():
                    corpus[doc] = corpus[doc] + ' ' + Loader.value(doc, key)
            else:
                for attr in attrs:
                    corpus[doc] = corpus[doc] + ' ' + Loader.value(doc, attr)
            
            corpus[doc] = corpus[doc].strip().replace('\n', '')
        return corpus