import os
import csv

file_tag_freq = open('../generatedFiles/tag_freq.csv', 'r')
file_word_freq = open('../generatedFiles/word_freq.csv', 'r')
file_word_given_tag_probability = open('../generatedFiles/data4.csv', 'r')

csv_tag_freq = csv.reader(file_tag_freq)
csv_word_freq = csv.reader(file_word_freq)
csv_word_given_tag_probaility = csv.reader(file_word_given_tag_probability)

dict_tag_freq = {}
dict_word_freq = {}
dict_word_given_tag_probability = {}

for tag in csv_tag_freq:
    dict_tag_freq[tag[0]] = tag[1]

for word in csv_word_freq:
    dict_word_freq[word[0]] = word[1]

for probability in csv_word_given_tag_probaility:
    dict_word_given_tag_probability[probability[0]] = probability[1]


test_file = open('../Test-corpus/AN/AN0.xml')

import xml.etree.ElementTree as ET

mytree = ET.parse(test_file)
root = mytree.getroot()

correct = 0
total = 0

for element in list(root.iter('w'))[0:100]:
    word = element.text
    tag = element.attrib.get('c5')
    # tag_list = tag.split('-')
    # for tags in tag_list:
    #     file_append.write(word.rstrip() + "_" + tags + "\n")
    mx_p = -1
    tag_gen = ""
# P(T|W) = ( P(W|T) * P(T) ) / P(W)
    for tags in csv_tag_freq:
        word_given_tag = word + "|" + tags[0]
        P = 0
        if(word in dict_word_freq):
            P = ( int(dict_word_given_tag_probability[word_given_tag]) * int(dict_tag_freq[tags[0]])) / int(dict_word_freq[word]) 
        if P > mx_p:
            tag_gen = tag[0]
    
    if tag == tag_gen:
        correct += 1
    else:
        print(word + "\t" + tag +'\t' + tag_gen)

    if tag.find('-'):
        if tag.split('-')[0] == tag or tag.split('-')[1] == tag:
            correct += 1
    total += 1


print(correct)
print(total)