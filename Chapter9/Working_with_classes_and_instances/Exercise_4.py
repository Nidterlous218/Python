"""
Start with your program from Exercise 9-1. Add an attribute called 
number_served with a default value of 0. Create an instance called 
restaurant from this class. Print the number of customers the restaurant 
has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number 
and print the value again. Add a method called increment_number_served() 
that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent 
how many customers were served in, say, a day of business."""




class Restaurant():
    """ A simple info about the restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize restaurant_name and cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Print the restaurant's name and cuisine type. """
        print("The name of the restaurant: " + self.restaurant_name.title())
        print("The cuisine type: " + self.cuisine_type + ".\n")

    def open_restaurant(self):
        """ State out the restaurant is open. """
        print(self.restaurant_name.title() + " is open!!!\n")

    def set_number_served(self, number_served):
        """ change the number of customers served."""

        if number_served >= self.number_served:
            self.number_served = number_served
        
        else:
            print("You can't decrease the number of customers served\n")
        
    def increment_number_served(self, increment):
        """Update the number of customers served."""
        self.number_served += increment
    
    def show_number_served(self):
        """Print the number of customers served."""
        print("The restaurant has served: " + str(self.number_served) + 
        " customers.\n")

restaurant = Restaurant("Mcdonald", "Western")
restaurant.describe_restaurant()
restaurant.set_number_served(50)
restaurant.show_number_served()
restaurant.increment_number_served(100)
restaurant.show_number_served()
