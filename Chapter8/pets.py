def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
describe_pet("dog", 'willie')    #Be aware of the order of the arguments as you will get funny results.

describe_pet(animal_type='cat', pet_name = 'lilly')


def describe_pet_dog(pet_name, animal_type='dog'):    #Default values for animal_type as dog
    """Display information about a specific pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_dog(pet_name = 'david')
describe_pet_dog(pet_name = 'ron', animal_type = 'hamster')

