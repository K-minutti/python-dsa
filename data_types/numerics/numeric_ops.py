'''
Included are some numeric ops you may want to perform
'''
import math
import random

# Absolute Value
abs(-34.5)

# Ceiling 
math.ceil(2.17)

# Floor
math.floor(3.14)

# Minimum of two numbers
x = 5
min(x, -4)

# Maximum of two numbers
y = 3.1111
max(3.14, y)

# Power 
pow(2.71, 3.14)
2.71 ** 3.14

# Root
math.sqrt(225)

# Converting between Integers and Strs
str(42)
int('42')
float('2.71')

# Integers are infinite percision in python Floats are not
# so we can use Floats to represent infinity
float('inf')
float('-inf')

# Floats comparison
# isclose() is roboust when handling very large values and abs differences
# TODO: CHECK what else is out there
math.isclose(2.718280000, 2.718210000)

# Random
random.randrange(28)
random.randint(8, 16)
random.random()
a = [1, 2, 3, 4, 5]
random.shuffle(a)
random.choice(a)











