simple_foods = ('carve meats', 'egg omelets', 'salads', 'spaghettis', 'porridges')
print("\nThis is the five simple foods provided by buffet-style restaurant: ")
for food in simple_foods:
    print(food.title())

# simple_foods[0] = 'noodles' ==> This wouldn't work

changed_simple_foods = ('noodles', 'steaks' , 'salads', 'spaghetti', 'porridges')
print("\nThis is the five simple foods changed: ")
for food in changed_simple_foods:
    print(food.title())