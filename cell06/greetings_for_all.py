#!/usr/bin/env python3
def greeting(name = "noble stranger"):
    if isinstance(name,str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")
greeting("Alexander")
greeting("wil")
greeting()
greeting(42)
