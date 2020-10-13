import os
import csv
import operator

file_open = open("../generatedFiles/data1.txt", "r")

myList = file_open.read().splitlines()

word_dict = {}
tag_dict = {}
# import sys
for element in myList:
    # if (element.find('_') == -1):
    #     print(element)
    #     sys.exit(0)
    temp = element.split("_")
    word = temp[0]
    tag = temp[1]

    if (word.find(',') != -1):
        word = '"' + word+'"'

    if (word in word_dict):
        word_dict[word] += 1
    else: 
        word_dict[word] = 1

    if (tag in tag_dict):
        tag_dict[tag] += 1
    else: 
        tag_dict[tag] = 1

word_dict_ordered = dict( sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True))
tag_dict_orderded = dict( sorted(tag_dict.items(), key=operator.itemgetter(1),reverse=True))

word_freq_output = open("../generatedFiles/word_freq.csv", "w")
tag_freq_output = open("../generatedFiles/tag_freq.csv", "w")

for key in word_dict_ordered.keys():
    word_freq_output.write("%s,%s\n" % (key, word_dict_ordered[key]))

for key in tag_dict_orderded.keys():
    tag_freq_output.write("%s,%s\n" % (key, tag_dict_orderded[key]))