guests = ['Doran', 'Sandie' , 'Anna']
guests.insert(0, 'David')
guests.insert(2, 'John')
guests.append('Tim')
print('\nHello ' + guests[0] + ' you are invited to attend a dinner.')
print('\nHello ' + guests[1] + ' you are invited to attend a dinner.')
print('\nHello ' + guests[2] + ' you are invited to attend a dinner.')
print('\nHello ' + guests[3] + ' you are invited to attend a dinner.')
print('\nHello ' + guests[-2] + ' you are invited to attend a dinner.')
print('\nHello ' + guests[-1] + ' you are invited to attend a dinner.')
print("\nHello everyone, I found a bigger dinner table. Therefore, there will be more friends invite to attend this dinner.")

print(len(guests))