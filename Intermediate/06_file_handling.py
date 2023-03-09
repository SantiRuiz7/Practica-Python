### File Handling ###

import xml
import csv
import json
import os

# .txt file
txt_file = open("Intermediate/my_file.txt", "w+")
print(txt_file.read())
# print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
