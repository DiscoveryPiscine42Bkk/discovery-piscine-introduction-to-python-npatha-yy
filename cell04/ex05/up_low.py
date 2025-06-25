#!/usr/bin/env python3
j=""
n = input()
for char in n:
    if (char.isupper() == True):
        j += char.lower()
    else:
        j += char.upper()
print(j)
