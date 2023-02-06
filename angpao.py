prompt = "Please insert every amount of the money from your angpaos: "
prompt += "(Enter 'end' to exit the progress of insert)"
money_amount = []

prompt_active = True

while prompt_active:
    collected_amount = input(prompt)

    if collected_amount == 'end':
        prompt_active = False

    else:
        money_amount.append(collected_amount)

   
print (money_amount)
total_amount = 0
for money in money_amount:
    if money == ' ' or money == '':
        continue

    else:
        total_amount += int(money)

print("Your total money in angpao is: " + str(total_amount)) 