# ex15.py
"""
Exercise 15 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

from sys import argv

# unpack command line arguments into variables
script, filename = argv

# open the file specified by the filename
txt = open(filename)

# print the file to std out
print "Here's your file %r:" % filename
print txt.read()

# ask the user for a file name
print "Type the filename again:"
file_again = raw_input("> ")

# open the file specified by the user
txt_again = open(file_again)

# print that file to std out
print txt_again.read()

# close files
txt.close()
txt_again.close()

