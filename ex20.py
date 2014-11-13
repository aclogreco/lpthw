# ex20.py
"""
Exercise 20 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

from sys import argv

# unpack cmd line arguments
script, input_file = argv

# print out the contents of file f
def print_all(f):
    print f.read()


# set file cursor position to the begining of file f
def rewind(f):
    f.seek(0)


# print a line from file f
def print_a_line(line_count, f):
    print line_count, f.readline()


# open the file for reading
current_file = open(input_file)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now, let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

