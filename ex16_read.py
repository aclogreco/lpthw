# ex16_read.py
"""
Exercise 16 -- Study Drill 2 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

from sys import argv

# unpack cmd line arguments
script, filename = argv

# open the file to be read
txt = open(filename)

# print the contents of the file to std out
print txt.read()

# close the file
txt.close()

