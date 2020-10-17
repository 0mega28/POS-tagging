import os
import csv

file_tag_freq=open('../generatedFiles/tag_freq.csv','r')
file_word_freq=open('../generatedFiles/word_freq.csv','r')
file_word_tag_freq=open('../generatedFiles/data2.csv','r')

dict_tag_freq={}
list_word_freq=[]
dict_word_tag_freq={}

tagfreq=csv.reader(file_tag_freq)
wordfreq=csv.reader(file_word_freq)
wordtagfreq=csv.reader(file_word_tag_freq)

for word in wordfreq:
    list_word_freq.append(word)

for tag in tagfreq:
    dict_tag_freq[tag[0]]=tag[1]

for word_tag in wordtagfreq:
    dict_word_tag_freq[word_tag[0]]=word_tag[1]

probability_of_word_given_tag={}
# P(Word|Tag) = P(Word^Tag)/P(Tag) = Count(Word_Tag)/Count(Tag)

for word in list_word_freq:
    for tag in dict_tag_freq.keys():
        temp=word[0]+"_"+tag
        temp1=word[0]+"|"+tag
        probability_of_word_given_tag[temp1]=dict_word_tag_freq[temp]/dict_tag_freq[tag]
        
print(probability_of_word_given_tag)




file_tag_freq.close()
file_word_freq.close()
file_word_tag_freq.close()
