import json

file_name = 'favourite_number.json'

def get_stored_number():
    """Try to get the number from the file if available."""
    try:
        with open(file_name) as f_obj:
            number = json.load(f_obj)
    
    except FileNotFoundError:
        return None
    
    else:
        return number

def store_number():
    """Prompt the user for his favourite number."""
    prompt = input("Please enter your favourite number: ")
    test_number = check_number(prompt)
    with open(file_name, 'w') as f_obj:
        json.dump(test_number, f_obj)
    return test_number
    


def check_number(number):
    """Check if the input is a number."""
    try:
        number = int(number)

    except ValueError:
        print("That's not a number!")
        retry = interface()
    else:
        return number

def interface():
    number = get_stored_number()

    if number:
        print("Found it! Your favourite number is " + str(number) + "!!!")
    
    else:
        number = store_number()
        print("Number stored. Your favourite number is: " + str(number) + ".")


interface()










































    


