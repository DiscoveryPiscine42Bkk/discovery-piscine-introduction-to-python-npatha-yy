#!/usr/bin/env python3
import sys
parameter = sys.argv[1:]
if not parameter:
    print("none")
else:
    for x in parameter:
        if not x.endswith("ism"):
            print(x+"ism")
