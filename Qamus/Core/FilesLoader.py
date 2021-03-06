#!/usr/bin/python
# -*- coding=utf-8 -*-
class FileLoader:
    @staticmethod
    def readFile(fileName, encoding="utf-8"):
        with open(fileName, 'r', encoding=encoding) as file:
            data = file.read().replace('\n', '')
        return data

    @staticmethod
    def readFiles(filesNames, encoding="utf-8"):
        data = dict()
        for filename in filesNames:
            data[filename] = FileLoader.readFile(filename, encoding)
        return data

    @staticmethod
    def loadStopWords(fileName, encoding="utf-8"):
        data = list()
        with open(fileName, 'r', encoding=encoding) as file:
            data = file.readlines()
        data = [elem.replace("\n", "") for elem in data]
        return data
