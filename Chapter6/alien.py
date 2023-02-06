alien0 = {'color': 'green', 'points': 5}

print(alien0['color'].title())
print(alien0['points'])

new_points = alien0['points']
print("\nYou just earned " + str(new_points) + " points!")

alien0['x_position'] = 0
alien0['y_position'] = 25
print(alien0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n The alien is " + alien_0['color'])
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_1['x_position']))

#Move the alien to the right
#Determine how far to moce the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

#The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New x-position: " + str(alien_1['x_position']))

print(alien0)
del alien0['points']
print(alien0)