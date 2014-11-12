# ex19.py
"""
Exercise 19 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

# cheese_and_crackers function definition
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# my own function that computes factorials and prints the result
def factorial(n):
    print "%d! =" % n,
    result = 1
    while (n > 0):
        result = result * n
        n -= 1
    print "%d" % result


print "We can just give the function numbers directly:"
# pass numbers as arguments to the function
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# pass variables as arguments to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# pass the results of the maths to the function
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# essentially, pass the results of the maths to the function, again...
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 1: literal as an argument
factorial(100)

# 2: math
factorial(((10 + 3) * 7) / 2)

# 3: variable
num = 23
factorial(num)

# 4: variable + maths
num = 88
factorial(num / 4)

# 5: user input
num = int(raw_input("Enter an integer: "))
factorial(num)

