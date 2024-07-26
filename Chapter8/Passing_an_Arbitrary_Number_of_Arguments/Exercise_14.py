""" Write a function that stores information about a car in a 
dictionary. The function should always receive a manufacturer and a model 
name. It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value 
pairs, such as a color or an optional feature """

def car_info(manufacture, model, **details):

    car = {}
    car['manufacture'] = manufacture
    car['car_model'] = model
    for key, value in details.items():
        car[key] = value
    return car

car_1 = car_info('Tesla', 'Model S', color='blue', optional_feature='autopilot')

print(car_1)