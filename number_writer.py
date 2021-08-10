import json

numbers = [3, 2, 6, 4, 15, 7, 11]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)