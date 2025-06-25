#!/usr/bin/env python3
import sys

if len(sys.argv)-1 !=1:
    print("none")
else:
    word = sys.argv[1]
    user = input("What was the parameter?")
    if user== word:
        print("Good job")
    else:
        print("Nope, sorry...")
