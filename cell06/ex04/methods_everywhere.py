#!/usr/bin/env python3
import sys

def shrink(n):
    print(n[:8])

def enlarge(n):
    print(n + "Z" * (8 - len(n)))
if len(sys.argv)-1 < 1:
    print("none")
else:
    for x in sys.argv[1:]:
        if len(x) < 8:
            enlarge(x)
        elif len(x) > 8:
            shrink(x)
        else:
            print(x)

