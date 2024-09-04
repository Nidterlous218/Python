file_path = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Reading_from_a_file/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents + "\n")

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

