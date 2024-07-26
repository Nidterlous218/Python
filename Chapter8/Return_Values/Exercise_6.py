def city_country (city, country):
    """Shows the name of the city and its country."""
    city_names = city.title() + ", " + country.title()
    return city_names

while True:
    print("Please enter a city name and its country:")
    print("Enter q to exit the loop")
    city = input("The city: ")
    if city == 'q':
        break

    country = input("The country: ")
    if country == 'q':
        break

    shows_results = city_country(city, country)
    print(shows_results)
