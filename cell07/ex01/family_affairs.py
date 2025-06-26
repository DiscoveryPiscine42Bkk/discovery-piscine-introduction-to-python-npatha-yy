#!/usr/bin/env python3
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

def find_the_redheads(f):
    x = []
    for key,value in dupont_family.items():
        if value == "red":
            x.append(key)
    return x

print(find_the_redheads(dupont_family))
