import os
import xml.etree.ElementTree as ET

file_append = open("../generatedFiles/data1.txt", "w")


for subdir, dirs, files in os.walk(r'../Train-corpus'):
    for filename in files:
        filepath = subdir + os.sep + filename
        mytree = ET.parse(filepath)
        root = mytree.getroot()

        # Handled mw tags
        for element in root.iter('mw'):
            mw_words = ""
            for words in element.iter('w'):
                mw_words += words.text
            tag = element.attrib.get('c5')
            file_append.write(mw_words.rstrip() + "_" + tag + "\n")

        # Handled w tags
        for element in root.iter('w'):
            word = element.text
            tag = element.attrib.get('c5')
            tag_list = tag.split('-')
            for tags in tag_list:
                file_append.write(word.rstrip() + "_" + tags + "\n")

        # Handled c tags
        for element in root.iter('c'):
            file_append.write(element.text.rstrip() + "_" + element.attrib.get('c5') + "\n")

# mw tags i.e. multiword there are tags init
# c tags i.e. puctuations
# if tag1-tag2 then word_tag1, word_tag2
# Handle the spacing 
# Don't take words from hw tags