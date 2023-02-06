prompt = "Please enter your pizza toppings."
prompt += "\n(Enter 'quit' to exit.):  "

pizza_toppings = []

while True:
    message = input(prompt)

    if message == "quit":
        pizza_toppings.append('nothing')
        break

    pizza_toppings.append(message)
    print(pizza_toppings)

print("\nHere is the list of your ordered pizza toppings:")
for topping in pizza_toppings:
    if topping == 'nothing':
        print("\nThere aren't any pizza toppings added yet.")
    else:
        print("\n\t" + topping.title())

