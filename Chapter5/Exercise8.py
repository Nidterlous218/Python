usernames = ['admin', 'chronoti', 'razuri', 'picninghi', 'setche']
for username in usernames:
    if username == 'admin':
        print("Hello " + usernames[0].title() + ", would you like yo see a status report?")
    else:
        print("\nHello " + username.title() + ", thank you for logging in again.")