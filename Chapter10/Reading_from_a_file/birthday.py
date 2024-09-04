file_path = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Reading_from_a_file/pi_million_digits.txt'

with open(file_path) as file_object:
    content  = file_object.readlines()

pi_string = ''
for line in content:
    pi_string += line.strip()

birthday = input("Enter your birthdat, in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")