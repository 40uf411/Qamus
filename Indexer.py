from collections import Counter
from Tokenizer import Tokenizer


class Indexer:

    @staticmethod
    def indexDoc(doc, stopWords):
        tokens = Tokenizer.tokenize(doc[1], stopWords)
        vocab = Tokenizer.defineVocabulary(tokens)
        return (doc[0], vocab)

    @staticmethod
    def indexDocs(docs, stopWords):
        data = list()
        for doc in docs:
            data.append(Indexer.indexDoc(doc, stopWords))
        return data

    @staticmethod
    def mergedIndexes(indexes):
        # getting a list of all the terms
        c = Counter()
        for index in indexes:
            c.update(list(index[1].keys()))
        # creating a dict that contains all the terms and their frequency in the docs
        data = dict()
        for term in c.keys():
            data[term] = dict()
            for index in indexes:
                data[term][index[0]] = 0
        # updating the frequency
        for index in indexes:
            for _ in range(len(index[1])):
                term = index[1].popitem()
                data[term[0]][index[0]] = term[1]
        return data
