"""An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant():
    """ A simple info about the restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Print the restaurant's name and cuisine type. """
        print("The name of the restaurant: " + self.restaurant_name.title())
        print("The cuisine type: " + self.cuisine_type.title() + ".\n")

    def open_restaurant(self):
        """ State out the restaurant is open. """
        print(self.restaurant_name.title() + " is open!!!\n")

class IceCreamStand(Restaurant):
    """A simple info of the ice cream."""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """Initialize ice cream flavor."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        """Describe the flavors of the ice cream."""
        print("We have these flavors available: ")

        for flavor in self.flavors:
            print("- " + flavor.title())

restaurant = IceCreamStand("coffee terrace", "western buffet", "chocolate", "vanilla", "mint")
restaurant.describe_restaurant()
restaurant.describe_flavors() 