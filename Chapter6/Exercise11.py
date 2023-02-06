cities = {'sydney': {'country': 'australia',
                     'population': '5.312 million(2019)',
                     'fact': 'more than 100 beaches.'},
         'dushanbe': {'country': 'tajikistan',
                      'population': '770,027(2013)',
                      'fact': 'built around picturesque parklands.'},
         'boston': {'country': 'united states',
                    'population': '654,776(2021)',
                    'fact': 'named after a town in england.'},
        }

for city, city_informations in cities.items():
    print("\nThe information of " + city.title() + " included its country, population, and interesting fact.")
    print("\tCountry: " + city_informations['country'].title())
    print("\tPopulation: " + city_informations['population'])
    
    if city == 'sydney':
        print("\tInteresting fact: " + city.title() + " has " + city_informations['fact'])
    
    else:
        print("\tInteresting fact: " + city.title() + " was " + city_informations['fact'])