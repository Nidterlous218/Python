pizzas = ['hawaian chicken', 'beef peperoni', 'mushrooms']
friend_pizzas = pizzas[:]
pizzas.append('seafood delight')
friend_pizzas.append('smoky bbq')

print("\nMy favourite pizzas are :")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title())