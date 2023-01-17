locations = ['paris', 'london', 'tokyo', 'amazon', 'denmark']
print(locations)

print("\nThis is the sorted list of locations")
print(sorted(locations))

print("\nThe list is still in its original order")
print(locations)

print("\nThis is the reverse sorted list of locations")
print(sorted(locations, reverse=True))

print("\nThe list is still in its original order")
print(locations)

print("\nThe list of locations is in reverse order")
locations.reverse()
print(locations)

print("\nThe list of locations is back to its original order")
locations.reverse()
print(locations)

print("\nThe list of locations is sort.")
locations.sort()
print(locations)

print("\nThe list of locations is sort reversely.")
locations.sort(reverse=True)
print(locations)


