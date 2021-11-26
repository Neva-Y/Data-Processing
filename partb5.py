## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import numpy
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import dot
from numpy.linalg import norm

#Function to acquire the ID of the document of the text file
def get_documentID(path, filename):
    pattern = r'[A-Z]{4}-\d{3}(?=[A-Z]{2})[A-Z]|[A-Z]{4}-\d{3}(?=[A-Z]\W)[A-Z]|[A-Z]{4}-\d{3}[A-Z]$|[A-Z]{4}-\d{3}'
    with open(os.path.join(path, filename), 'r') as f:
            for line in f:
                if (re.findall(pattern, line)):
                    return (re.findall(pattern, line))
                
#Function to preprocess the text file
def preprocess_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
        #Lowercase 
        text = text.lower()
        #Remove non-alphabetic except spacing characters
        text = re.sub(r'[^a-zA-Z \t\n\r]', '', text)
        text = re.sub(r'\t{1,}|\n{1,}|\r{1,}', ' ', text)
        text = re.sub(r' {2,}', ' ', text)
        text = re.sub(r' $', '', text)
        return text

#Function to stem a sentence into word tokens
def stem_sentence(text):
    tokenWords=word_tokenize(text)
    stemSentence=[]
    for word in tokenWords:
        stemSentence.append(porter.stem(word))
        stemSentence.append(" ")
    return "".join(stemSentence)


#Preprocess the input keywords and stemming them
porter = PorterStemmer()
keyWords = numpy.empty(len(sys.argv)-1, dtype=object)
for i in range(len(keyWords)):
    keyWords[i] = sys.argv[i+1].lower()
    keyWords[i] = re.sub(r'[^a-z]', '', keyWords[i])
    keyWords[i] = porter.stem(keyWords[i])

#Create corpus of all the documents that contains the given keywords
maxFiles = 999
documents = 0
textIDs = numpy.empty(maxFiles, dtype=object)
corpus = numpy.empty(maxFiles, dtype=object)
path = (os.getcwd() + "/Cricket/")
for filename in os.listdir(path):
    if re.match("\d{1,}\.txt", filename):
        filepath = (path + filename)
        text = preprocess_text(filepath)
        text = stem_sentence(text)
        matches = 0
        for i in range (len(keyWords)):
            if keyWords[i] in text:
                matches = matches + 1
            if matches == len(keyWords):
                textIDs[documents] = get_documentID(path, filename)
                corpus[documents] = text
                documents = documents + 1

#Resize arrays to the number of documents found
textIDs = numpy.resize(textIDs, documents)
corpus = numpy.resize(corpus, documents)

#Exit program if there are no documents found
if documents == 0:
    sys.exit('No documents found containing the keywords')

#Create TFIDF matrix for the corpus of documents    
vect = TfidfVectorizer()
tfidf_matrix = vect.fit_transform(corpus)
tfidfDF = pd.DataFrame(tfidf_matrix.toarray(), columns = vect.get_feature_names())
uniqueWords = vect.get_feature_names()

#Create vector of counts for the keywords with all the unique words from the corpus
keywordVector = numpy.zeros(len(uniqueWords))
for i in range(len(uniqueWords)):
    for j in range(len(keyWords)):
        if uniqueWords[i] == keyWords[j]:
            keywordVector[i] = keywordVector[i] + 1
        
#Calculate the cosine similarity of each document with the keywords vector        
tfidfDF = tfidfDF.to_numpy()
cosineSimilarity = numpy.empty(len(textIDs), dtype=object)
for i in range(len(textIDs)):
    cosineSimilarity[i] =  round(dot(tfidfDF[i], keywordVector)/(norm(tfidfDF[i])*norm(keywordVector)),4)

#Changing the index of the data frame to the Document IDs and sorting it in descending order
cosineSimilarityDF = pd.DataFrame({'documentID':textIDs, 'score':cosineSimilarity})
cosineSimilarityDF = cosineSimilarityDF.set_index('documentID')
cosineSimilarityDF = cosineSimilarityDF.sort_values(by=['score'],ascending=False)
print(cosineSimilarityDF)