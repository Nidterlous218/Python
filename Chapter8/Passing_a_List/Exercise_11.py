""" Start with your work from Exercise 8-10. Call the 
function make_great() with a copy of the list of magicians’ names. 
Because the original list will be unchanged, return the new list and 
store it in a separate list. Call show_magicians() with each list to 
show that you have one list of the original names and one list with 
the Great added to each magician’s name. """

def make_great(original_magicians, copy_original_magicians):
    """Modify the list of magicians by adding 'the Great' to each magician's name."""

    while original_magicians:
        copy = original_magicians.pop()
        copy_original_magicians.append(copy)

    for i in range(len(copy_original_magicians)):
        copy_original_magicians[i] = "the Great " + copy_original_magicians[i]

    
def show_magicians(names):
    for name in names:
        print(name.title())

original_magicians = ['harry housini', 'david coppedfield', 'derren brown']
copy_original_magicians = []
make_great(original_magicians[:], copy_original_magicians)

print("\nThe Original: ")
show_magicians(original_magicians)

print("\nThe Copy: ")
show_magicians(copy_original_magicians)
