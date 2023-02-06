rivers = {'nile': 'egypt',
        'amazon river': 'brazil',
        'ganges': 'india',}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe following is the famous rivers:")
for river in sorted(rivers.keys()):
    print(river.title())

print("\nThe following is the rivers flow through the countries:")
for country in sorted(rivers.values()):
    print(country.title())