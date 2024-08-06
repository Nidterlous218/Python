"""An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method.
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

class Admin(User):

    """Stores the attributes of a privileges action for the admin user."""
    def __init__(self, first_name, last_name, *privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges
    
    def show_privileges(self):
        """Print the attributes of a privileges action."""

        print("The admin has the following privileges: ")

        for attribute in self.privileges:
            print("- " + privileges)

user1 = Admin("mu ping", "liew", "can ban user", "can add user", "can delete post")
user1.show_privileges()
