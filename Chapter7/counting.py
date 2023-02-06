current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n")

current_numbers  = 0
while current_numbers < 10:
    current_numbers += 1

    if current_numbers % 2 == 0:
        continue

    else:
        print(current_numbers)