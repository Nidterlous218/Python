requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
    
print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings: # list use in if statement will return true(at least one item) or false(no item), help to determine if the list is empty
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")