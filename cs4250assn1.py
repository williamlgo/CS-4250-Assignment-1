#-------------------------------------------------------------------------
# AUTHOR: William Go
# FILENAME: cs4250assn1.py
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: 8 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
    if i > 0: # skipping the header
      documents.append (row[0].lower())

print("Document Values: ")
print(documents)

for i in range(3):
  documents[i] = documents[i].split()
print("Getting rid of Spaces: ")
print(documents)

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'they', 'their', 'them', 'theirs', 'she', 'her', 'hers', 'he', 'him', 'his', 'i', 'you', 'for', 'and', 'but', 'or', 'so'}

#getting rid of stopwords
for word in stopWords:
  for i in range(len(documents)):
    for isterm in documents[i]:
      if(word == isterm):
        documents[i].remove(word)

print("Removing Stop Words: ")
print(documents)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "love" : "loves",
    "dog" : "dogs",
    "cat" : "cats"
}

key_list = list(stemming.keys())
val_list = list(stemming.values())

for key, val in stemming.items():
  for i in range(len(documents)):
    for j in range(len(documents[i])):
      if(val == documents[i][j]):
        #Get the key
        position = val_list.index(val)
        documents[i][j] = key

print("Stemming (replace variants with its stem):")
print(documents)

#Identifying the index terms.
#--> add your Python code here
terms = []
for i in range(len(documents)):
  for isterm in documents[i]:
    if(isterm not in terms):
      terms.append(isterm)
print("Terms: ")
print(terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = [[0]*3]*3

#Getting the total count of documents
totaldocuments = len(documents)
idfs = []
tfs = [[0]*3]*len(terms)

#Calculating idf
for k in range(len(terms)):
  idfcount = 0
  for i in range(len(documents)):
    for isterm in documents[i]:
      idfcount = idfcount + 1
  idf = math.log(idfcount/totaldocuments)
  idfs.append(idf)

#Calculating tf
for i in range(len(documents)):
  for k in range(len(terms)):
    termcount = 0
    for j in range(len(documents[i])):
      if(terms[k] == documents[i][j]):
        termcount = termcount + 1
    tfs[i][k] = termcount/len(documents[i])

#Calculating tf.idf
for i in range(len(documents)):
  for j in range(len(idfs)):
    docTermMatrix[i][j] = tfs[i][j] * idfs[j]

#Printing the document-term matrix.
#--> add your Python code here
print("\nDocument Term Matrix: ")
print("       love   cat   dog")
for i in range(len(docTermMatrix)):
  rowstring = "Row " + str(i) + ": "
  for j in range(len(docTermMatrix)):
    rowstring = rowstring + str(docTermMatrix[i][j]) + "      "
  print(rowstring)
