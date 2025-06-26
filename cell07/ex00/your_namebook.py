#!/usr/bin/env python3
def array_of_names (name):
    x = []
    for first, last in name.items():
        x.append(f"{first.capitalize()} {last.capitalize()}")
    return x

persons = {
            "jean":"valjean",
            "grace":"hopper",
            "xavier":"niel",
            "fifi":"brindacier"
}
print(array_of_names(persons))
