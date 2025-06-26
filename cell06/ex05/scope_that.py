#!/usr/bin/env python3
def add_one(parameter):
    n = parameter + 1
    print("inside",n)
x=7
add_one(x)
print("after", x)

#The parameter inside the add_one function doesn’t affect the original variable x when add_one(x) is called.
