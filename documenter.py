#!/usr/bin/env python3
# Sorry this is not very feature heavy at the moment guys, it's a bit of a quick "hack-job" to help with
# some data recovery for a user
# FIXME Return usage if no argument is provided
# FIXME Change so that you can choose to display all text, or search for specific text in a file

#Import our modules
import sys
#Grab the important stuff from the docx module
from docx import opendocx, getdocumenttext
#Grab our dir_list function
import dir_list
phrase = input("What phrase do you wish to seach for? ")

#List variable is the actual list send back of directories from our dir_list module
list = dir_list.listing(sys.argv[1])

#For each item in our list, spit out the contents of said document
for listing in list:
    #Open the document from listing
    document = opendocx(listing)
    #Grab text from opened document
    textlist = getdocumenttext(document)
    #Search for the phrase case insensitively
    if any(phrase in s.lower() for s in textlist):
        print(phrase, "found in ", listing)
    #Print text, followed by document title
    #print(textlist, "FILENAME: ", listing)