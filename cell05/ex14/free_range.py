#!/usr/bin/env python3
import sys
parameter = sys.argv[1:]
if len(parameter) != 2:
    print("none")
else:
    x = int(parameter[0])
    y = int(parameter[1])
    print(list(range(x,y+1)))
