items = ['bottle', 'mouse', 'computer', 'pencil', 'paper']
print("The firs three items in the list are:")
for item in items[0:3]:
    print(item.title())
    

print("\nThree items from the middle of the list are: ")
for item in items[1:4]:
    print(item.title())

print("\nThe last three items in the list are: ")
for item in items[-3:]:
    print(item.title())