"""Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance."""

class Restaurant():
    """ A simple info about the restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Print the restaurant's name and cuisine type. """
        print("The name of the restaurant: " + self.restaurant_name.title())
        print("The cuisine type: " + self.cuisine_type + ".\n")

    def open_restaurant(self):
        """ State out the restaurant is open. """
        print(self.restaurant_name.title() + " is open!!!\n")

restaurant1 = Restaurant("the golden spoon", "italian")
restaurant2 = Restaurant("spice symphony", "indian")
restaurant3 = Restaurant("sakura delight", "japanese")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()