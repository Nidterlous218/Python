prompt = "How old are you?"
prompt += "\nThere are different ticket prices for several ages."
prompt += "\n\tfree for under 3 \t $10 for between 3 to 12 \t $15 for 12 above. "
prompt += "\n(Enter 'quit' to exit.) "

while True:

    prices = input(prompt)

    if prices == 'quit':
        print("Goodbye!!!")
        break

    else:
        prices = int(prices)
        if prices < 3:
            print("\nThe ticket is free for under 3 years old.\n")
        
        elif prices < 12:
            print("\nThe cost for the ticket is $10.\n")

        else: 
            print("\nThe cost for the ticket is $15.\n")