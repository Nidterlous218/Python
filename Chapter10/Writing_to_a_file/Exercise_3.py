file_name = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Writing_to_a_file/guest.txt'

with open(file_name, 'a') as file_object:
    while True:
        guest_name = input("Please enter your name (enter q to exit the loop): ")
        file_object.write(guest_name.title() + '\n')

        if guest_name.lower() == 'q':
            break