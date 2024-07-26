""" Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and 
a cuisine_type. Make a method called describe_restaurant() that 
prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the restaurant 
is open. Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods. """

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


restaurant = Restaurant("the great pizza palace", "italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
