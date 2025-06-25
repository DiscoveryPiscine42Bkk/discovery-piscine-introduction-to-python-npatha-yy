#!/usr/bin/env python3
import sys

if len(sys.argv)-1 !=2:
    print("none")
else:
    word = sys.argv[1]
    text = sys.argv[2]
    x = text.count(word)
    print(x)
