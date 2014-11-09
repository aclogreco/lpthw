# ex6.py
"""
Exercise 6 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

# use the format operator to place an integr in the string
x = "There are %d types of people." % 10
# assign strings to vaiables
binary = "binary"
do_not = "don't"
# use the format operator to place two strings within another string
y = "Those who know %s and those who %s." % (binary, do_not)

# print string x to standard output
print x
# print string y to standard output
print y

# print a string that has x placed in it using the object placeholder
print "I said: %r." % x
# print a string that has x placed in it using the string placeholder
print "I also said: '%s'." % y

# assign a boolean value to a variable
hilarious = False
# assign a string that contains a generic object placeholder to a variable
joke_evaluation = "Isn't that joke so funny?! %r"

# print a string that has a boolean value placed in it
print joke_evaluation % hilarious

# assign strings to variables
w = "This is the left side of..."
e = "a string with a right side."

# print a string which is the result of the concatenation of two strings
print w + e

