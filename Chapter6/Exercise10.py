favourite_numbers = {'prince stephenson': [83, 24, 3, 54],
                     'celine garner':[48, 43, 36],
                     'marlina archer':[69],
                     'lyndon calhoun':[10, 17, 47, 70, 84],
                     'steven barr':[5, 59],
                     }

for name, numbers in favourite_numbers.items():
    print("\nThis is " + name.title() + "'s favourite numbers: ")

    for number in sorted(numbers):
        print("\t" + str(number))