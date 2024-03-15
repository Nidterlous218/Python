def describe_city(city, country = 'USA'):
    if country == 'USA':
        print(city.title() + " is in " + country.upper())
    else:
        print(city.title() + " is in " + country.title())

describe_city('Sydney')
describe_city('New York')
describe_city('Kuala Lumpur', 'India')