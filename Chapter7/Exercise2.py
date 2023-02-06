request = "May I know how many people will have for the dinner group? "
request += "\nBecause if there are more than eight people, you'll have to wait for a table."

number = input(request + "\n\tTotal numbers: ")

if int(number) >= 8:
    print("You'll have to wait for a table.")

else:
    print("Your table is ready.")
