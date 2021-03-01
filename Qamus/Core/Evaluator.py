from .SearchEngine import SearchEngine

class Evaluator:
    sampleSize = 0
    dataSize = 0
    y = list()
    yP = list()
    @staticmethod
    def init(queries, results, similarityMethod = SearchEngine.INNER_PRODUCT_SIMILARITY, minRel=1e-10):
        Evaluator.sampleSize = len(queries)
        Evaluator.y = results
        inSearch = list()
        for query in queries:
            inSearch.append(
                SearchEngine.search(
                    request=query,
                    model=SearchEngine.VECTOR_MODEL,
                    options={
                        'similarityMethod': similarityMethod,
                        'minRel': minRel,
                        'dict': True
                    })
            )
        Evaluator.yP = inSearch
        return

    @staticmethod
    def accuracy(r=None):
        yP = Evaluator.yP[:r]
        y = Evaluator.y
        results = dict()
        for i in range(len(y)):
            if i >= len(yP):
                break 
            results[i] = list()
            yp = yP[i].keys()
            for elem in y[i]:
                if int(elem) in yp:
                    results[i].append(int(elem))
        recallList = list()
        for i in range(len(results)):
            if len(results[i]) == 0:
                recallList.append(0)
            else:
                recallList.append(len(results[i]) / len(yP[i]))
        return sum(recallList) / len(recallList)

    @staticmethod
    def recall(r=None):
        yP = Evaluator.yP[:r]
        y = Evaluator.y
        results = dict()
        for i in range(len(y)):
            if i >= len(yP):
                break 
            results[i] = list()
            yp = yP[i].keys()
            for elem in y[i]:
                if int(elem) in yp:
                    results[i].append(int(elem))
        recallList = list()
        for i in range(len(results)):
            recallList.append(len(results[i]) / len(y[i]))
        return sum(recallList) / len(recallList)

    @staticmethod
    def fScore(r=None):
        acc = Evaluator.accuracy(r)
        recall = Evaluator.recall(r)
        return (2 * acc * recall) / (acc + recall)

    @staticmethod
    def eScore(beta, r=None):
        acc = Evaluator.accuracy(r)
        recall = Evaluator.recall(r)
        return ((1 + beta ** 2) * acc * recall) / (((beta ** 2) * acc) + recall)

    @staticmethod
    def dcg():
        pass