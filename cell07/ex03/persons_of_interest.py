#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(women):
    n =  list(women.items())
    def get_birth(N):
        return N[1]["date_of_birth"]
    n.sort(key = get_birth)
    for x, y in n:
            print(f"{y["name"]} is a great scientist born in {y["date_of_birth"]}")

famous_births(women_scientists)
