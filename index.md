# Qamus

<div style="text-align:center">
<img src="logo.png" alt="SemaWal logo" style="width:250px;"/>
</div>

Qamus is an information retrieval tool that allows for documents indexing, similarity calculation, and search operations with both boolean and vector models.

Developper:  Ali AOUF

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/40uf411/Qamus/master/AUTHORS.md)
Release  | 0.1
License  |[GMP](https://github.com/40uf411/Qamus/master/LICENSE)
Tracker  |[40uf411/Qamus/Issues](https://github.com/40uf411/Qamus/issues)
Source  |[Github](http://github.com/40uf411/Qamus)
Feedbacks  |[Comments](https://github.com/40uf411/Qamus/)
Accounts  |[@Twitter](https://twitter.com/40uf411)

##  Features:
* Text tokenization.
* Documents indexing.
* Similarity calculation:
    * Inner product.
    * Dice coefficient.
    * Cosinus.
    * Jaccard index.
* Search models:
    * Boolean model.
    * Vector model.
* One end-point being the search engine.
* Ready-to-use datasets:
    * CACM (English corpus).
    * Faranja (French corpus).
* Save and load search engines (indexes, pre-processed data).

##  Use cases:
* Search engine for a blog, a store, or a document related software.
* Documents indexation.
* Information retrieval.
* Corpus analysis.


---

## Changelog:
#### 0.1 (06.02)
        - First release

---
## Guide
### Install
```shell
pip install qamus
```
#### [requirements]
Qamus requires no lib 😉️😊️
```
None, Nada, Rien...
```

### Import
```python
>>> from Qamus.Core.SearchEngine import SearchEngine
>>> from Qamus.Datasets.CACM.Api import Loader
```
### Load the corpus from the CACM dataset
```python
>>> corpus = Loader.corpus('T', 'W', 'A')
```
### Create a list of stop-words or import the NLTK English stop-words
```python
>>> import nltk
>>> nltk.download('stopwords')
>>> from nltk.corpus import stopwords
```
### Build the search engine
```python
>>> SearchEngine.init(
        dataset=corpus, 
        stopwords=stopwords.words('english')
    )
```
### Search using the boolean model
```python
>>> result = SearchEngine.search(
        request='set and computer or ( test or algorithm )', 
        model=SearchEngine.BOOLEAN_MODEL
    )
>>> print(result[:10])
# [29, 30, 70, 71, 103, 112, 124, 125, 126, 127]
```
### Search using the vector model
```python
>>> result = SearchEngine.search(
        request='set of algorithms or logical normal tests', 
        model=SearchEngine.VECTOR_MODEL, 
        options = {
            'similarityMethod': SearchEngine.JACCARD_INDEX_SIMILARITY
        }
    )
>>> print(list(result.items())[:3])
# pairs of (document, similarity-index)
# [(70, 0.00048037208105415364), (71, 6.166909620313026e-05), (94, 0.0003457159774689914)]
```

---

## Datasets
Qamus 0.1 comes by default with two datasets:
### CACM
The CACM collection is a collection of titles and abstracts from the journal CACM. If memory serves, a number of the articles reference each other. [(Documentation)](http://ir.dcs.gla.ac.uk/resources/test_collections/cacm/)
The CACM collection comes with 3204 document written in English.
To load and import data from CACM, you only have to import the `Loader` class.
```python
>>> from Qamus.Datasets.CACM.Api import Loader
>>> docs = Loader.loadData()
```
Each document in the CACM collection has a list of attributes. Not all documents share the same set of attributes. Qamus has a built in function that allows the user to create a corpus of clean text from a list of CACM attributes.
```python
>>> corpus = Loader.corpus('T', 'W', 'A')
```
Qamus has also a list of built in function that allows you to manipulate and extract specific data from this corpus.
```python
>>> doc = loader.doc(15) # return the document with id = 15
>>> doc = loader.value(15, 'T') # return the value of the attribute 'T' from the document with id = 15
```
### Faranja
Faranja is a collection of french 15 novels and documented from around 1830 to 2015.
The Faranja collection was collected by [the developers of Qamus](github.com/40uf411) and it also comes with a list of french stopwords.
Similar to CACM, importing Faranja is as easy as importing a class.
```python
>>> from Qamus.Datasets.Faranja.Api import Loader
>>> docs = Loader.loadData()
```
Since the collection of Faranja has no attributes the data obtained from the loaded dataset can be used as a corpus, and to avoid confusion, the `corpus` function can be used here as well to return Faranja corpus
```python
>>> corpus = Loader.corpus()
```
Faranja also comes with some useful function that gives a background to the documents in the collection.
```python
>>> doc = loader.doc(15) # return the document with id = 15
>>> doc = loader.value(15, 'Title') # return the title 'T' from the document with id = 15
>>> doc = loader.titles() # return the titles of the documents
>>> doc = loader.titleOf(15) # return the title of the documents with id = 15
```
You can also import the french stopwords that come with Faranja by calling the `stopwords()` function.
```python
>>> corpus = Loader.stopwords()
```
## Indexing
## Tokenizing
## Search operations
### Search engine
### Search models
#### Boolean model:
#### Vector model:
**Similarity functions:**
* Inner product:
* Dice coefficient:
* Cosinus
* Jaccard index

