#!/usr/bin/python
# -*- coding=utf-8 -*-
import os 
from ..Dataset import Dataset

class Loader(Dataset):

    init = False
    data = dict()
    stopwords = list()
    
    DOCS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/docs/'
    DOCS = {
        '0': {
            'title': 'Le Seigneur Des Anneaux (Intégral) by Tolkien J R R.',
            'location': DOCS_DIR + 'D0.txt'
            },
        '1': {
            'title': 'Dits et écrits III - 1976-1979 by Michel Foucault.',
            'location': DOCS_DIR + 'D1.txt'
            },
        '2': {
            'title': 'Linvestissement immobilier locatif intelligent by Julien Delagrandanne.',
            'location': DOCS_DIR + 'D2.txt'
            },
        '3': {
            'title': 'Naissance de la clinique by Michel Foucault.',
            'location': DOCS_DIR + 'D3.txt'
            },
        '4': {
            'title': 'Histoire De Juliette by de Sade Marquis.',
            'location': DOCS_DIR + 'D4.txt'
            },
        '5': {
            'title': 'Les Aventures Deraste Fandorine (Intégral) by Akounine Boris.',
            'location': DOCS_DIR + 'D5.txt'
            },
        '6': {
            'title': 'La Grammaire Est Une Chanson Douce by Orsena Eric.',
            'location': DOCS_DIR + 'D6.txt'
            },
        '7': {
            'title': 'Le réseau bouclier Le danger arctique by Ludlum Robert.',
            'location': DOCS_DIR + 'D7.txt'
            },
        '8': {
            'title': 'Alexandre Le Grand Tome 1 by Valerio Manfredi.',
            'location': DOCS_DIR + 'D8.txt'
            },
        '9': {
            'title': 'La Terreur Des Abysses by Alten Steve.',
            'location': DOCS_DIR + 'D9.txt'
            },
        '10': {
            'title': 'Le Cercle Celtique by Larson Bjôrn.',
            'location': DOCS_DIR + 'D10.txt'
            },
        '11': {
            'title': 'Le Vétéran by Forsyth Frederik.',
            'location': DOCS_DIR + 'D11.txt'
            },
        '12': {
            'title': 'Noir Dessin by Parsons Julie.',
            'location': DOCS_DIR + 'D12.txt'
            },
        '13': {
            'title': 'Orm Le Rouge (Intégral) by Begston Hans G.',
            'location': DOCS_DIR + 'D13.txt'
            },
        '14': {
            'title': 'Un Si Beau Mensonge by Martin David.',
            'location': DOCS_DIR + 'D14.txt'
            },
    }
    DOCS_ENCODING = 'ISO-8859-1'
    STOPWORDS_FILE = os.path.dirname(os.path.realpath(__file__))  + '/stopwords_fr.txt'
    STOPWORDS_ENCODING = 'utf-8'
    
    @staticmethod
    def titles():
        titles = list()
        for doc in Loader.DOCS.values():
            titles.append(doc['title'])
        return titles

    @staticmethod
    def titleOf(id):
        return Loader.DOCS[id]['title'] if id in Loader.DOCS.keys() else ''

    @staticmethod
    def __readFile(fileName, encoding="utf-8"):
        with open(fileName, 'r', encoding=encoding) as file:
            data = file.read().replace('\n', '')
        return data

    @staticmethod
    def loadData():
        if not Loader.init:
            for id, doc in Loader.DOCS.items():
                Loader.data[id] = Loader.__readFile(doc['location'], Loader.DOCS_ENCODING)
            
            data = list()
            with open(Loader.STOPWORDS_FILE, 'r', encoding=Loader.STOPWORDS_ENCODING) as file:
                data = file.readlines()
            data = [elem.replace("\n", " ") for elem in data]
            Loader.stopwords = data
        
            Loader.init = True
        return Loader.data

    @staticmethod
    def corpus(*attrs):
        return Loader.loadData()

    @staticmethod
    def stopwords():
        Loader.loadData()
        return Loader.stopwords

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