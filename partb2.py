## Part B Task 2
import re
import sys
import numpy
import os

path = (os.getcwd() + "/Cricket/002.txt")
with open(path, 'r') as file:
    text = file.read()
    #Lowercase 
    text = text.lower()
    #Remove non-alphabetic except spacing characters
    text = re.sub(r'[^a-zA-Z \t\n\r]', '', text)
    #Replace spacing characters to whitespace
    text = re.sub(r'\t{1,}|\n{1,}|\r{1,}', ' ', text)
    #Replace 2 or more consequtive whitespaces with single whitespace
    text = re.sub(r' {2,}', ' ', text)
    #Remove whitespace at the end of the text file
    text = re.sub(r' $', '', text)
    print(text)