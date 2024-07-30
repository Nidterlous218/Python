"""
Add an attribute called login_attempts to your User class from 
Exercise 9-3 (page 166). Write a method called increment_login_attempts() 
that increments the value of login_attempts by 1. Write another method 
called reset_login_attempts() that resets the value of login_attempts 
to 0. Make an instance of the User class and call 
increment_login_attempts() several times. Print the value of 
login_attempts to make sure it was incremented properly, and then call 
reset_login_attempts(). Print login_attempts again to make sure it was 
reset to 0
"""

class User():
    """ Represents a user simple profile. """

    def __init__(self, first_name, last_name, *infos):
        """ Initialize user's attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.infos = infos
        self.login_attempts = 0

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
    
    def increment_login_attempts(self):
        """Increment the login attempt by 1"""
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        """Reset the login attempt to 0"""
        self.login_attempts = 0
        return self.login_attempts

user = User("MP", "Liew")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(str(user.login_attempts))
user.reset_login_attempts()
print(str(user.login_attempts))