dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250   ==> This wouldn't work since tuple can' change elements

print("\nOriginal dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 10)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)