import os
import csv

file_word_tag_freq = open('../generatedFiles/data2.csv', 'r')
file_tag_freq = open('../generatedFiles/tag_freq.csv', 'r')
file_word_freq = open('../generatedFiles/word_freq.csv', 'r')

dict_word_tag_freq = {}
dict_tag_freq = {}
list_word_freq = []

wordtagfreq = csv.reader(file_word_tag_freq)
tagfreq = csv.reader(file_tag_freq)
wordfreq = csv.reader(file_word_freq)

for word_tag in wordtagfreq:
    dict_word_tag_freq[word_tag[0]] = word_tag[1]

for tag in tagfreq:
    dict_tag_freq[tag[0]] = tag[1]

for word in wordfreq:
    list_word_freq.append(word)

probability_of_word_given_tag = {}

# P(Word|Tag) = P(Word^Tag)/P(Tag) = Count(Word_Tag)/Count(Tag)

for word in list_word_freq:
    for tag in dict_tag_freq.keys():
        temp = word[0]+"_"+tag
        temp1 = word[0]+"|"+tag
        if temp1.find(',') != -1:
            temp1 = '"' + temp1 + '"'
        if (temp in dict_word_tag_freq):
            probability_of_word_given_tag[temp1] = int(dict_word_tag_freq[temp]) / int(dict_tag_freq[tag])
        else:
            probability_of_word_given_tag[temp1] = 0

output_file = open("../generatedFiles/data4.txt", "w")

for key in probability_of_word_given_tag.keys():
    output_file.write("%s,%s\n" % (key, probability_of_word_given_tag[key]))

file_word_tag_freq.close()
file_tag_freq.close()
file_word_freq.close()