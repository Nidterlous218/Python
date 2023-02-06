sandwich_orders = []
order = "Please order you sandwich: "
order += "(Type 'quit' to exit)"

while True:
    cart = input(order)

    if cart == 'quit':
        print("Goodbye! Its is happy to serve for you.")
        break
    else:
        sandwich_orders.append(cart)

finished_sandwiches = []

while sandwich_orders:
    done = sandwich_orders.pop()

    finished_sandwiches.append(done)

print("\nThe sandwiches you had ordered has been ready.")
for sandwich in finished_sandwiches:
    print("\tI had made you a " + sandwich.title() + " sandwich.\n")
