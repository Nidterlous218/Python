""" Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in 
Exercise 9-7. Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
"""

class User():

    """ Represents a user simple profile. """

    def __init__(self, first_name, last_name, **infos):
        """ Initialize user's attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.infos = infos
        self.login_attempts = 0

    def describe_user(self):
        """ Print a summary of the user's information: """
        complete_name = self.first_name + ' ' + self.last_name
        print("Name: " + complete_name.title())
        for key, value in self.infos.items():
            print(key + ": " + value.title())
        print("\n")
        
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

class Privileges():
    """Stores the list of privileges action."""
    def __init__(self, privileges = ['can ban user', 'can add user', 'can delete user']):
        self.privileges = privileges
        
    def show_privileges(self):
        """Print the attributes of a privileges action."""

        print("The admin has the following privileges: ")

        for privilege in self.privileges:
            print("- " + privilege)
        
        print("\n")

class Admin(User):

    """Stores the attributes of a privileges action for the admin user."""
    def __init__(self, first_name, last_name, **infos):
        super().__init__(first_name, last_name, **infos)
        self.privileges = Privileges()


admin = Admin("tom", "sun", country = "UK", gender = "male", age = "50")
admin.describe_user()
admin.privileges.show_privileges()

