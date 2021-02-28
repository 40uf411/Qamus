#!/usr/bin/python
# -*- coding=utf-8 -*-
import os 
from ..Dataset import Dataset

class Loader(Dataset):

    init = False
    data = dict()
    evaluation = dict()

    @staticmethod
    def loadData():
        if not Loader.init:
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
            Loader.data = data
            # loading the evaluation relations
            data = dict()
            with open(dir_path + '/qrels.text', 'r') as file:
                lines = file.readlines()
            id = ''
            key = ''
            for line in lines:
                line = line.split()
                if int(line[0]) not in data.keys():
                    id = int(line[0])
                    data[id] = dict()
                    data[id]['result'] = list()
                data[id]['result'].append(line[1])
            Loader.evaluation = data
            # loading the evaluation queries
            eq = dict()
            with open(dir_path + '/query.text', 'r') as file:
                lines = file.readlines()
            id = ''
            key = ''
            for line in lines:
                if line[0:2] == '.I':
                    id = int(line[3:].strip())
                    eq[id] = dict()
                elif line[0] == '.':
                    key = line[1:].strip()
                    eq[id][key] = ''
                else:
                    eq[id][key] = eq[id][key] + line
            for key, val in eq.items():
                if key in Loader.evaluation.keys():
                    Loader.evaluation[key]['query'] = val
            Loader.init = True    
        return Loader.data

    @staticmethod
    def doc(id):
        if not Loader.init:
            Loader.loadData()
        
        data = Loader.data[id] if (id in Loader.data.keys()) else dict()
        return data

    @staticmethod
    def value(docID, key):
        doc = Loader.doc(docID)
        return doc[key] if key in doc.keys() else ''
    
    @staticmethod
    def corpus(*attrs):
        Loader.loadData()
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

    @staticmethod
    def evaluationQueries(keys = [], seperat = False):
        Loader.loadData()
        if seperat:
            data = dict()
            data['queries'] = list()
            data['results'] = list()
            for key, query in Loader.evaluation.items():
                data['results'].append(query['result'])
                if len(keys) > 0:
                    s = ''
                    for key, val in query['query'].items():
                        if key in keys:
                            s = s + str(val)
                    data['queries'].append(s)
                else:
                    data['queries'].append(query['query'])
            return data
        else:
            return Loader.evaluation