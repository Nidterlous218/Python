motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'    # to replace a element, just replce a new element with the corresponding index
print(motorcycles)

motorcycles.append('bmw')    # the append will add a new element in the last
print(motorcycles)

brand = []                   # the append function could also help to build a new list
brand.append('honda')
brand.append('yamaha')
brand.append('suzuki')
print(brand)

motorcycles.insert(0, 'honda') # the insert function help to append a new element into certain index(any position)
print(motorcycles)

del motorcycles[0]              # the delete function help to remove any element at any index(any position
print(motorcycles)
del motorcycles[2]              # the index is according to the new list after the first del
print(motorcycles)

popped_motorcycles = motorcycles.pop() # the pop let you remove the last element in the list, and let you use in for other use.
print(motorcycles)
print(popped_motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycles.upper() + ".")

first_owned = motorcycles.pop(0)       # the pop func could also point to the certain index, just like the del, and insert func.
print("The first motorcycle I owned was " + first_owned.title() + ".")

print(motorcycles)
motorcycles.remove('yamaha')        # We can also remove the element by using remove function and the value inside the list.
print(motorcycles)
