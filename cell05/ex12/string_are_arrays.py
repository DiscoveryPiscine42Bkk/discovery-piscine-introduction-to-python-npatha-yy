#!/usr/bin/env python3

import sys
x = sys.argv[1:]
if len(x) != 1:
    print("none")
else:
    z =x[0]
    y = 0
    for char in z:
        if char == "z":
             print("z", end="")
             y+=1
    if y ==0:
        print("none")
