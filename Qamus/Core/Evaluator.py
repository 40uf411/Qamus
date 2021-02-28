from .SearchEngine import SearchEngine

class Evaluator:
    sampleSize = 0
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
    def accuracy():
        pass

    @staticmethod
    def recall():
        pass

    @staticmethod
    def fScore():
        pass