# ex5.py
"""
Exercise 5 -- Learn Python the Hard Way -- Zed A. Shaw 
A.C. LoGreco
"""

name = 'Anthony C. LoGreco'
age = 32
height = 66.0  # inches
weight = 185.0  # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# Convert height and weight into SI units.
height_si = height * 2.54  # convert inches into centimeters
weight_si = weight * (1 / 2.2046226218) # convert pounds into kilograms

print "Let's talk about %s." % name
print "He's %d inches tall or %.2f centimeters tall." % (height, height_si)
print "He's %d pounds heavy or %.2f kilograms heavy." % (weight, weight_si)
print "Actually that's not too heavy. ;-)"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee. ;-)" % teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

