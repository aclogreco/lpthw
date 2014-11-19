# ex33.py
"""
Exercise 33 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

def makeNumList(count, inc):
    """Creates a list from 0 to (count - 1) incremented by inc"""
    i = 0
    numList = []
    
    while i < count:
        print "At the top i is %d" % i
        numList.append(i)
        i += inc
        print "Numbers now: ", numList
        print "At the bottom i is %d" % i
    
    return numList


numbers = makeNumList(10, 2)
print "The numbers: "
for num in numbers:
    print num

numbers = makeNumList(8, 3)
print "The numbers: "
for num in numbers:
    print num

numbers = makeNumList(6, 1)
print "The numbers: "
for num in numbers:
    print num

