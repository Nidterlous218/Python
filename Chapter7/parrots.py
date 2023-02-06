prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = " "

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

    else:
        print("Goodbye!")


cue = "\nTell me something, and I will repeat it back to you: "
cue += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(cue)

    if message == 'quit':
        active = False
    
    else: 
        print(message)