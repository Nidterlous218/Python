def city_country_name(city, country, population = ""):
    """Display the name of the city and its belong country."""
    if population:
        string = city.title() + ", " + country.title() + " - population " + str(population) + "."
    
    else:
        string = city.title() + ", " + country.title() + "."
    return string
