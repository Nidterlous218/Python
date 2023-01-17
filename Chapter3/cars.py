cars = ['bmw','audi','toyota','subaru']

print("Here is the original list.")
print(cars)

print("\nHere is the sorted list.")  # It sorted in this print function, but remain the same order in the list.
print(sorted(cars))
print(cars)

cars.reverse() # Reverse the order of the list
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(len(cars))   # It shwows the amount of the elements in the list