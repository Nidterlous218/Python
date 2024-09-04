file_path = 'C:/Users/liewm/OneDrive/Desktop/Python\Chapter10/Reading_from_a_file/learning_python.txt'

with open(file_path) as file_content:
    lines = file_content.readlines()

strings = ''
for line in lines:
    strings += line.lstrip()

print(strings)
print("\n")

changes = ''
for line in lines:
    changes += line.replace('Python', 'C')
    
print(changes)
