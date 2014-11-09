# ex8.py
"""
Exercise 8 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    formatter % (1, 2, 3, 4), 
    formatter % ("one", "two", "three", "four"), 
    formatter % (True, False, False, True), 
    formatter % (formatter, formatter, formatter, formatter)
)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

