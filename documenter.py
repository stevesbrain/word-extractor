#!/usr/bin/env python3
# FIXME Return usage if no argument is provided

#Import our modules
import sys
#Grab the important stuff from the docx module
from docx import opendocx, getdocumenttext
#Grab our dir_list function
import dir_list

#List variable is the actual list send back of directories from our dir_list module
list = dir_list.listing(sys.argv[1])

#For each item in our list, spit out the contents of said document
for listing in list:
    #Open the document from listing
    document = opendocx(listing)
    #Grab text from opened document
    textlist = getdocumenttext(document)
    #Print text, followed by document title
    print(textlist, "FILENAME: ", listing)