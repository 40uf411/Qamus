#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import re
import string
from collections import Counter

class Tokenizer:
    @staticmethod
    def tokenize(text, stopWords):
        text = text.lower()
        # remove special characters
        for c in "@!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            text = text.replace(c, ' ')
        # split into tokens by white space
        tokens = str(text).split()
        # remove punctuation from each token
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        # filter out empty words
        #tokens = [word for word in tokens if len(word) > 0]
        # filter out stopwords
        tokens = [word for word in tokens if word not in stopWords]
        if len(tokens) == 0:
            tokens = ['ukn']
        return tokens

    @staticmethod
    def defineVocabulary(tokens):
        vocab = Counter()
        vocab.update(tokens)
        # print('> Vocabulary size: %d\n' % len(vocab))
        return vocab
