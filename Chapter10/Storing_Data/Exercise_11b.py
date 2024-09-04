import json

file_name = 'favourite_number.json'
with open(file_name) as f_obj:
    number = json.load(f_obj)
    print("I know your favourite number! It's " + str(number) + ".\n")