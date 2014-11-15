# ex27.py
"""
Exercise 27 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

# Since I already have memorized the truth tables previously, I decided to make
# a small program to print out the truth tables.

print "Truth tables:\n"

# NOT
a = True
print "NOT:\n-----------------"
print " a\t| NOT(a)"
print "--------|--------"
print " %s\t| %s" % (a, not a)
a = False
print " %s\t| %s" % (a, not a)

