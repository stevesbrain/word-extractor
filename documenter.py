#!/usr/bin/env python3
import sys
from docx import opendocx, getdocumenttext
import dir_list

list = dir_list.listing(sys.argv[1])
num = 1
for listing in list:
    document = opendocx(listing)
    textlist = getdocumenttext(document)
    print(textlist)