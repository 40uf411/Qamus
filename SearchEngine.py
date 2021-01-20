class SearchEngine:
    index = None
    __init = False
    @staticmethod
    def init(index, corpus):
        SearchEngine.__index = index 
        SearchEngine.__corpus = corpus 
        SearchEngine.__init = True
    
    @staticmethod
    def lookUpFor(term, minOccurrences=1):
        # entry gates
        if not SearchEngine.__init:
            return False
        if term not in SearchEngine.__index.keys():
            return False
        # getting the docs that has a minimum occurrences of the term
        d = SearchEngine.__index[term]
        data = dict()
        for elem in SearchEngine.__index[term].keys():
            if d[elem] >= minOccurrences:
                data[elem] = d[elem]
        return data
    
    @staticmethod
    def IDF(term, fraction=True):
        if fraction:
            return len(SearchEngine.lookUpFor(term))/len(SearchEngine.__corpus)
        else:
            return len(SearchEngine.lookUpFor(term))
        