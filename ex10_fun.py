# ex10_fun.py
"""
A fun little code snippet.
Exercise 10 -- Learn Python the Hard Way -- Zed A. Shaw
A.C. LoGreco
"""

import time
import sys

while True:
    for i in ["/", "-", "\\", "|", "/", "-", "\\", "|"]:
        print "%s\r" % i,
        sys.stdout.flush()
        time.sleep(.1)

