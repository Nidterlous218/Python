"""Write a function that accepts a list of items a person wants 
on a sandwich. The function should have one parameter that collects 
as many items as the function call provides, and it should print a 
summary of the sandwich that is being ordered. Call the function three 
times, using a different number of arguments each time."""

def make_sandwich(*items):

    print("\nSandwich ordered:")
    for item in items:
        print("-" + item)

make_sandwich("bread", "lettuce", "tomato", "cheese", "pickles")
make_sandwich("cheese")
make_sandwich("tuna", "potato", "sausage")