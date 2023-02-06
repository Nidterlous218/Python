request = "Please enter a number, I'll told you whether the number is the multiplication of 10. "

number = input(request + "\n\tPlease enter here: ")

if int(number) % 10 == 0:
    print("This is the multiplication of 10.")

else:
    print("It should be the multiplication of other numbers.")