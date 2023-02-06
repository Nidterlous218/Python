alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Make an empty list for storing aliens.
aliensssss = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliensssss.append(new_alien)

for alien in aliensssss[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
#Show the first 5 aliens:
for alien in aliensssss[:5]:
    print(alien)
print(".....")

#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliensssss)))
