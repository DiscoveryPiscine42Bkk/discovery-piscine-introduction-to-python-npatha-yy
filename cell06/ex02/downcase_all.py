#!/usr/bin/env python3
import sys

def n (s):
    return s.lower()

if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        print(n(x))
else:
    print("none")
