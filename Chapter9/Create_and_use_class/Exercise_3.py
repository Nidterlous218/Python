"""Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints 
a summary of the user’s information. Make another method called 
greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both 
methods for each user."""

class User():
    """ Represents a user simple profile. """

    def __init__(self, first_name, last_name, *infos):
        """ Initialize user's attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.infos = infos

    def describe_user(self):
        """ Print a summary of the user's information: """
        complete_name = self.first_name + ' ' + self.last_name
        print("Name: " + complete_name.title())
        for info in self.infos:
            print("-" + str(info))
        
    def greet_user(self):
        """ Print a personalized greeting to the user. """
        complete_name = self.first_name + ' ' + self.last_name
        print("\nHello " + complete_name.title() + "!!!")

my_name = User("MP", "Liew", "Male", 12)
my_name.describe_user()
my_name.greet_user()