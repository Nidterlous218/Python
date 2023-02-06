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


print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    print("\nWe are very sorry, the deli has run out of pastrami, we'll help to remove it from the cart.")
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
