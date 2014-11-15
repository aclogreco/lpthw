# ex27.py
"""
Exercise 27 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

# Since I already have memorized the truth tables previously, I decided to make
# a small program to print out the truth tables.

print "Truth tables:\n"

# NOT
a = False
print "NOT:\n-----------------"
print " a\t| NOT(a)"
print "--------|--------"
print " %s\t| %s" % (a, not a)
a = True
print " %s\t| %s\n" % (a, not a)

# OR
a = False
b = False
print "OR:\n-------------------------"
print " a\t| b\t| a OR b"
print "--------|-------|--------"
print " %s\t| %s\t| %s" % (a, b, a or b)
b = True
print " %s\t| %s\t| %s" % (a, b, a or b)
a = True
b = False
print " %s\t| %s\t| %s" % (a, b, a or b)
a = True
b = True
print " %s\t| %s\t| %s" % (a, b, a or b)
