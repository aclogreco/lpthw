# ex21.py
"""
Exercise 21 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 2)
height = subtract(72, 6)
weight = multiply(95, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

also  = age + (height - (weight * (iq / 2)))

print "Another way to calculate the puzzle: ",
print "32 + (66 - (190 * (50 / 2))) = %d" % also


