import pizza2

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#module_name.function_name()
#from module_name import function_name
#from module_name import function_0, function_1, function_2

print("\n================================\n")
from pizza2 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n================================\n")

#from module_name import function_name as fn
from pizza2 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n================================\n")

#import module_name as mn

import pizza2 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n================================\n")

#from module_name import *
"""Importing All functions in a module"""

from pizza2 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')