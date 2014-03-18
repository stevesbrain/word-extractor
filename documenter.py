#!/usr/bin/env python3
import sys
from docx import opendocx, getdocumenttext


document = opendocx(sys.argv[1])
textlist = getdocumenttext(document)
print(textlist)