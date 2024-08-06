""" Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery. You should 
see an increase in the car’s range.
"""


class Car():

    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles    

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 20):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this bettery provides."""
        if self.battery_size <= 70:
            range = 240
        
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery."""

        if self.battery_size < 85:
            self.battery_size = 85
        
        else:
            print("The battery is already at 85 kWh.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electtric car."""

        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank.")
    
test_tesla = ElectricCar("tesla", "t series", "2008")
test_tesla.get_descriptive_name()
test_tesla.battery.get_range()
test_tesla.battery.upgrade_battery()
test_tesla.battery.get_range()
test_tesla.battery.upgrade_battery()
