# ex16.py
"""
Exercise 16 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

from sys import argv

# unpack cmd line arguments
script, filename = argv

# print warning / instruction message to the user
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER (RETURN)."

raw_input("?")

# open the file specified by the cmd line arg
print "Opening the file..."
target = open(filename, 'w')

# delete the contents of the file if the file already exists
print "Truncating the file. Goodbye file contents!"
target.truncate()

print "Now I'm going to ask you for three lines."

# get 3 lines of content from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these lines to the file."

# write the content lines to the file
content = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(content)

# close the file
print "And finally, we close it."
target.close()

