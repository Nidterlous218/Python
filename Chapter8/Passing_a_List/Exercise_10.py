""" Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the 
list of magicians by adding the phrase the Great to each 
magician’s name. Call show_magicians() to 
see that the list has actually been modified."""

def make_great(magicians):
    """Modify the list of magicians by adding 'the Great' to each magician's name."""
    
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

def show_magicians(names):
    for name in names:
        print(name.title())

magicians = ['harry housini', 'david coppedfield', 'derren brown']
make_great(magicians)
show_magicians(magicians)