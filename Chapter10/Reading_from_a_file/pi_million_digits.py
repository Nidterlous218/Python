file_path = 'C:/Users/liewm/OneDrive/Desktop/Python/Chapter10/Reading_from_a_file/pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
