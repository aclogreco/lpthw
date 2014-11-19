# ex33.py
"""
Exercise 33 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

def makeNumList(count):
    """Creates a list from 0 to (count - 1)"""
    i = 0
    numList = []
    
    while i < count:
        print "At the top i is %d" % i
        numList.append(i)
        i += 1
        print "Numbers now: ", numList
        print "At the bottom i is %d" % i
    
    return numList


numbers = makeNumList(10)
print "The numbers: "
for num in numbers:
    print num

numbers = makeNumList(8)
print "The numbers: "
for num in numbers:
    print num

numbers = makeNumList(6)
print "The numbers: "
for num in numbers:
    print num

