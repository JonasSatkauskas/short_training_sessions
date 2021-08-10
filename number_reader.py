import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

for i in numbers:
    print(i)