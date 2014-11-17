#!env python

import fileinput
import re


LINE_ITEM = r"^\s*(\d{5}\s\d{2}\s\d{2}\s\d{3})\s+([\d\s\w\,\%\/\.\-\'\#]*)\s(\d+\.\d+)\s(\w+)"
CATEGORY = r"^[\.]{10}\s+(.*)"

for line in fileinput.input():
    category = re.match(CATEGORY, line)
    if category is not None:
        print category.group(1)
    data = re.match(LINE_ITEM, line)
    if data is not None:
        print "Item ID: {0}\n\tDescription: {1}\n\tPrice: {2}\n\tUnit: {3}".format(data.group(1), data.group(2).rstrip(), data.group(3), data.group(4))
