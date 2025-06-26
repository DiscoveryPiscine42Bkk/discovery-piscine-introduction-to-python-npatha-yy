#!/usr/bin/env python3
def n(student):
    x = sum(student.values())
    y = len(student)
    return x / y
class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {n(class_3B)}.")
print(f"Average for class 3C: {n(class_3C)}.")
