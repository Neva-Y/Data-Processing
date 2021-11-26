# Elements of Data Processing Assignment 1

Name: Goh Xing Yang

Student ID: 1001969


# Brief Description

**parta** python files used to analyse covid data in 2020. The analysis of data is in the owid-covid-2020-visual-analysis.pdf file.

**partb** python files are used to create search rankings using TF-IDF cosine similarity to given keywords nd documents that have been stemmed with porter and preprocessed using regex.

# Vocabulary

**TF-IDF or term frequency–inverse document frequency** is a numerical statistics which reflects how important a word is to a document. The TF-IDF value increases to the frequency of the word in the document, but is offset by the frequency of the word in the corpus, which reduces the weighting to common words in the corpus.

**Cosine similarity** is a measure of similarity between two vectors, in this case we use this as a search ranking to compare how similar the document is the the given keywords.


**Porter stemmer** is a stemming method that reduces a word to it's root by removing the morphological and inflexional endings from words in English.

#  Dependencies:

- Python 3
- re
- os
- sys
- pandas
- nltk
- numpy 
- sklearn

