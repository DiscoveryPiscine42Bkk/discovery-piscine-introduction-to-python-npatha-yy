#!/usr/bin/env python3
i = 0
while i <= 10:
    print(f"Table de {i}:", end="")
    j = 0
    while j<=10:
        print(f"{i * j}", end=" ")
        j+=1
    print("")
    i +=1
