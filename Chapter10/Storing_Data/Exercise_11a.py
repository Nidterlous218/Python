import json

favourite_number = "What is your favourite number? "
prompt = input(favourite_number)

try:
    number = int(prompt)
    print("Thank you, " + str(number) + " is a great number.")

except ValueError:
    print("This isn't a number, please input a number again!")

else:
    file_name = 'favourite_number.json'
    with open(file_name, 'w') as f_obj:
        json.dump(prompt, f_obj)
