file_path = 'C:/Users/liewm/OneDrive/Desktop/Python\Chapter10/Reading_from_a_file/learning_python.txt'

with open(file_path) as file_content:
    content = file_content.read()
    print(content + '\n')

with open(file_path) as file_content:
    for content in file_content:
        print(content.strip())
    
    print('\n')

with open(file_path) as file_content:
    lines = file_content.readlines()

for line in lines:
    print(line.strip())
