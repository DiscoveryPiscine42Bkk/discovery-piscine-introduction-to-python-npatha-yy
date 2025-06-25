#!/usr/bin/env python3
import sys

parameter = sys.argv[1:]
if not parameter:
    print("none")
else:
    print(f"parameter: {len(parameter)}")
    for x in parameter:
            print(f"{x}: {len(x)}")
