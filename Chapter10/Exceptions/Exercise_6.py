def additional(num1, num2):

    try:
        number1 = int(num1)
        number2 = int(num2)

        additional = int(num1) + int(num2)
    
    except ValueError:
        print("Please enter numbers only!!!")
    
    else:
        
        print("The sum of the two numbers is: " + str(additional))

first_number = input("The first number: ")
second_number = input("The second number: ")
additional(first_number, second_number)
