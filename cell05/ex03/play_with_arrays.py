#!/usr/bin/env python3
original_array = [2,8,9,48,8,22,-12,2]
new_array = []
for x in original_array:
    if x > 5:
        new_array.append(x+2)
print("Original.array: ",original_array)
new_array.remove(10)
print("New array: ", {new_array[3],new_array[2], new_array[0], new_array[1]})
