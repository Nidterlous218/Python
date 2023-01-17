numbers = list(range(1,10)) # the elements inside is integers, to display it should convert to strings

for number in numbers:
    if number == '1':
        message = 'st'
    elif number == '2':
        message = 'nd'
    elif number == '3':
        message = 'rd'
    else:
        message = 'th'
    print(str(number) + message)
