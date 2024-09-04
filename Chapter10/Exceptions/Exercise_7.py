def additional ():
    """A simple additional calculator."""

    bool = True
    while bool:

        try:
            num1 = int(input("Please enter the first number:(type q to exit): "))
            num2 = int(input("Please enter the second number:(type q to exit): "))
            
        except ValueError:
            print("The values for additional argument must be both numbers.")
        
        else:
            result = num1 + num2
            print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(result) + ".\n")

additional()