
responses = {}

while True:
    name = input("What is your name?")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("\nWould you like to let another person to fill the poll? (yes/ no) ")

    if repeat == 'no':
        break

print("\n\t---Poll Results---")
for name, response in responses.items():
    print("" + name.title() + " would like to go to " + response.title() + ".")



