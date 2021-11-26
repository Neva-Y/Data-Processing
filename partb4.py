## Part B Task 4
import re
import os
import sys
import nltk
import numpy
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize

#Function to acquire the ID of the document of the text file
def get_documentID(path, filename):
    pattern = r'[A-Z]{4}-\d{3}(?=[A-Z]{2})[A-Z]|[A-Z]{4}-\d{3}(?=[A-Z]\W)[A-Z]|[A-Z]{4}-\d{3}[A-Z]$|[A-Z]{4}-\d{3}'
    with open(os.path.join(path, filename), 'r') as f:
            for line in f:
                if (re.findall(pattern, line)):
                    print(re.findall(pattern, line))

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

#Preprocess and stem the given keywords
porter = PorterStemmer()
keyWords = numpy.empty(len(sys.argv)-1, dtype=object)
for i in range(len(keyWords)):
    keyWords[i] = sys.argv[i+1].lower()
    keyWords[i] = re.sub(r'[^a-z]', '', keyWords[i])
    keyWords[i] = porter.stem(keyWords[i])

path = (os.getcwd() + "/Cricket/")
for filename in os.listdir(path):
    #Find all the documents in the path
    if re.match("\d{1,}\.txt", filename):
        filepath = (path + filename)
        #Preprocess and stem the text in the document
        text = preprocess_text(filepath)
        text = stem_sentence(text)
        matches = 0
        #Print the document ID if the stemmed document contains all the stemmed keywords
        for i in range (len(keyWords)):
            if keyWords[i] in text:
                matches = matches + 1
            if matches == len(keyWords):
                get_documentID(path, filename)