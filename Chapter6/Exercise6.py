favourite_languages = {'jen': 'python', 
                        'sarah': 'c', 
                        'edward': 'ruby', 
                        'phil': 'python',
                        }

polls = ['edward', 'ron', 'jen', 'harry', 'phil', 'george', 'fred']

for people in sorted(polls):
    if people in sorted(favourite_languages.keys()):
        print(people.title() + ", thanks for the responding.")

    else:
        print(people.title() + ", here is a poll for you to take!!!.")
