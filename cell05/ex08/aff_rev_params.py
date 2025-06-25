#!/usr/bin/env python3
import sys
if len(sys.argv)-1 < 2:
    print("none")
else:
    for x in reversed(sys.argv[1:]):
        print(x)
