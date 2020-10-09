import os
import xml.etree.ElementTree as ET

file_append = open("../submission/data1.txt", "a")

import os

for subdir, dirs, files in os.walk(r'../Train-corpus'):
    for filename in files:
        filepath = subdir + os.sep + filename
        mytree = ET.parse(filepath)
        root = mytree.getroot()
        for element in root.iter('w'):
            word_tag = element.attrib.get('hw') + "_" + element.attrib.get('c5')
            file_append.write(word_tag + "\n")
