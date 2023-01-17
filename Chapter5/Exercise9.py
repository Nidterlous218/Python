usernames = ['admin', 'chronoti', 'razuri', 'picninghi', 'setche']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + usernames[0].title() + ", would you like yo see a status report?")
        else:
            print("\nHello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + usernames[0].title() + ", would you like yo see a status report?")
        else:
            print("\nHello " + username.title() + ", thank you for logging in again.")
else:
    print("\nWe need to find some users!") 