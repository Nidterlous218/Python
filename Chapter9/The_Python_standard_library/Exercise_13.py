from collections import OrderedDict

glossary = OrderedDict()

glossary['class'] = 'groups of definitions.'
glossary['for loop'] = 'a conditional function to keep looping'

for glossary, meanings in glossary.items():
    print("The meaning of the " + glossary + " is: " + meanings + ".")