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

print("\nEvryone, due to the insufficient space for guests and the arrival time of the dinner table won't be on the time. There will be two guests only.")
print(guests)
first_poped = guests.pop(1)
second_poped = guests.pop(2)
third_poped = guests.pop(-2)
final_poped = guests.pop(-1)
print("\nI am sorry " + first_poped.title() + ", there will be next time for a bigger table.")
print("\nI am sorry " + second_poped.title() + ", there will be next time for a bigger table.")
print("\nI am sorry " + third_poped.title() + ", there will be next time for a bigger table.")
print("\nI am sorry " + final_poped.title() + ", there will be next time for a bigger table.")
print("\nDear " + guests[0].title() + ", you will still attend the dinner with " + guests[-1].title() + ".")
print("\nDear " + guests[-1].title() + ", you will still attend the dinner with " + guests[0].title() + ".")
del guests[0]
del guests[-1]
print(guests)