rental_cars = ['dodge viper', 'chevrolet corvette', 'lamborghini countach', 'porche 911', ]

rent = ("What car do you want for rental? ")
rent += "We'll try to find the same car for your requirement "

decision = input(rent)

if decision in rental_cars:
    print("Let me see if I can find you a " + decision.title() + ".....")
    print("There's a " + decision.title() + ", please proceed for the rent.")

else:
    print("Sorr, we can't find you a " + decision.title() + ", maybe you should search from other rental cars companies.")
