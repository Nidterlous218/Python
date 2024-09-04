file_name = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Writing_to_a_file/guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        prompt = "What is your name: "
        prompt += "\n enter q to exit the loop: "

        name = input(prompt)
        if name =='q':
            break

        else:
            file_object.write(name.title() + " has attend the wedding.\n")
            print("Welcome " + name.title() + "!\n")
        

        

        
