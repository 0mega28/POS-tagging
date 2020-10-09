import os
import csv

file_open = open("../generatedFiles/data1.txt", "r")

myList = file_open.read().splitlines()

myDict = {}

for word in myList:
    if (word in myDict):
        myDict[word] += 1
    else:
        myDict[word] = 1

output_file = open("../generatedFiles/data2.csv", "w")

for key in myDict.keys():
    output_file.write("%s,%s\n"%(key,myDict[key]))

print(myDict)