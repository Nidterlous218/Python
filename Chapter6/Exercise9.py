favorite_places = {'kristina curtis': ['zambia', 'bonaire'],
                   'moses nolan': ['taiwan', 'solomon islands', 'sweeden'],
                   'katelyn hull': ['chad', 'pitcairn islands', 'wales'],
                   }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favourite places:")

    for place in places:
        print("\t" + place.title())