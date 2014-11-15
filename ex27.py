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
print " %s\t| %s" % (a, not a)

# OR
a = False
b = False
print "\nOR:\n-------------------------"
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

# AND
a = False
b = False
print "\nAND:\n--------------------------"
print " a\t| b\t| a AND b"
print "--------|-------|---------"
print " %s\t| %s\t| %s" % (a, b, a and b)
b = True
print " %s\t| %s\t| %s" % (a, b, a and b)
a = True
b = False
print " %s\t| %s\t| %s" % (a, b, a and b)
a = True
b = True
print " %s\t| %s\t| %s" % (a, b, a and b)

# NOT OR
a = False
b = False
print "\nNOT OR:\n------------------------------"
print " a\t| b\t| NOT(a OR b)"
print "--------|-------|-------------"
print " %s\t| %s\t| %s" % (a, b, not (a or b))
b = True
print " %s\t| %s\t| %s" % (a, b, not (a or b))
a = True
b = False
print " %s\t| %s\t| %s" % (a, b, not (a or b))
a = True
b = True
print " %s\t| %s\t| %s" % (a, b, not (a or b))

# NOT AND
a = False
b = False
print "\nNOT AND:\n-------------------------------"
print " a\t| b\t| NOT(a AND b)"
print "--------|-------|--------------"
print " %s\t| %s\t| %s" % (a, b, not (a and b))
b = True
print " %s\t| %s\t| %s" % (a, b, not (a and b))
a = True
b = False
print " %s\t| %s\t| %s" % (a, b, not (a and b))
a = True
b = True
print " %s\t| %s\t| %s" % (a, b, not (a and b))

# XOR
a = False
b = False
print "\nXOR:\n--------------------------"
print " a\t| b\t| a XOR b"
print "--------|-------|---------"
print " %s\t| %s\t| %s" % (a, b, a ^ b)
b = True
print " %s\t| %s\t| %s" % (a, b, a ^ b)
a = True
b = False
print " %s\t| %s\t| %s" % (a, b, a ^ b)
a = True
b = True
print " %s\t| %s\t| %s" % (a, b, a ^ b)

# !=
a = 0
b = 0
print "\n!= :\n-------------------------"
print " a\t| b\t| a != b"
print "--------|-------|--------"
print " %d\t| %d\t| %s" % (a, b, a != b)
b = 1
print " %d\t| %d\t| %s" % (a, b, a != b)
a = 1
b = 0
print " %d\t| %d\t| %s" % (a, b, a != b)
a = 1
b = 1
print " %d\t| %d\t| %s" % (a, b, a != b)

