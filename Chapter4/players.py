players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # just the first three players
print(players[1:4])
print(players[2:])  # strart with index 2


print("\nHere are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
 