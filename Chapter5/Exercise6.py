age = 65

if age < 2:
    message = 'baby'
elif age < 4:
    message = 'toddler'
elif age < 13:
    message = 'kid'
elif age < 20:
    message = 'teenager'
elif age < 65:
    message = 'adult'
else:
    message = 'elder'

if message == 'adult' or message == 'elder':
    print("You are an " + message + ".\n")
else:
    print("You are a " + message + ".\n")