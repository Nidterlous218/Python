def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " doesn't exist."
        print(msg)
    
    else:
        #Count approximate number of words in the file.abs
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words.")

file_name = 'alice_in_wonderland.txt'
count_words(file_name)