file_name = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Writing_to_a_file/reasons.txt'

with open(file_name, 'w') as file_object:
    prompt = "What's the reason of loving to programming? "
    prompt += "(Enter q to exit the loop.)\n"

    while True:
        reason = input(prompt)

        if reason == 'q':
            break
        else:
            file_object.write(reason + "\n")