## Part B Task 1
import re
import pandas as pd
import os
import sys
import numpy

#Regex pattern for the document ID
pattern = r'[A-Z]{4}-\d{3}(?=[A-Z]{2})[A-Z]|[A-Z]{4}-\d{3}(?=[A-Z]\W)[A-Z]|[A-Z]{4}-\d{3}[A-Z]$|[A-Z]{4}-\d{3}'

#Initialising the arrays and variable counting the number of documents
numFiles = 0
maxFiles = 999
documentName = numpy.empty(maxFiles, dtype=object)
documentID = numpy.empty(maxFiles, dtype=object)

#Get path to text files and loop through all the text files that satisfy regex pattern
path = (os.getcwd() + "/Cricket/")
for filename in os.listdir(path):
    if re.match("\d{1,}\.txt", filename):
        with open(os.path.join(path, filename), 'r') as f:
            for line in f:
                if (re.findall(pattern, line)):
                    documentName[numFiles]=filename
                    documentID[numFiles]= re.findall(pattern, line)
                    numFiles = numFiles + 1

#Resize array to number of text files and creating a data frame to save to csv                    
documentName = numpy.resize(documentName, numFiles)    
documentID = numpy.resize(documentID, numFiles)
documentData = pd.DataFrame({'filename':documentName, 'documentID':documentID})
documentData = documentData.sort_values(by=['filename'])
documentData = documentData.set_index('filename')
documentData.to_csv(sys.argv[1])