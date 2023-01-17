current_users = ['ben', 'paul', 'fred', 'george', 'harry']
new_users = ['jane', 'fred', 'george', 'hermione', 'ron']

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("You need to enter a new username since there's someone registered with that username.\n")
    else:
        print("The username is available, please proceed to register.\n")