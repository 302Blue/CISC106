# Random numbers
from random import *

# randint()
number = randint(1, 100)
print(number)

def roll():
    value = randint(1, 6)
    return value

print(roll())
print(roll())

# randrange()
print(randrange(1, 3, 1))
print(randrange(1, 10))
print(randrange(10))

# random()
print(random())
print(random())

# uniform()
print(uniform(0.0, 9.0))
print(uniform(2.0, 5.0))

# seed() - sets a starting point for the pseudo-random number generator.
# Setting the seed to a previously used value will give the exact same
# sequence of random numbers that was obtained when the seed was previously
# used.
seed(10)

for n in range(5):
    print(random())


# Nested for loops
# This inner loop runs to completion once for every value in the outter loop
# In this case the outter loop runs for two values, so the inner loop run to
# completion two time. The inner loop also runs two time whenever it runs,
# so the print statement in the inner loop is executed 2 * 2 = 4 times.
for m in [1, 2]:
    for n in ['a', 'b']:
        print(m, n)

# Create a multiplication table
for x in range(1, 13):
    for y in range(1, 13):
        print(format(x * y, '5d'), end = '')
    print()


# Testing type
x = '5.0'
if type(x) == int:
    print('x is an int')
else:
    print('x is not an int')

# The if-statement is attempting to use a shortcut that won't work. This
# if statment will consider all values of x to be a number, even if it is
# not a number.
x = 5.0
if type(x) == int or float:
    print('x is a number')
else:
    print('x is not a number')

# Here is the correct way to test whether or not x is a number.
x = 5.0
if type(x) == int or type(x) == float:
    print('x is a number')
else:
    print('x is not a number')


# Functions returning multiple values
# Note that the number of varialbes avaiable to receive values must exactly
# match the number of values returned by the function.
def my_func(x):
    x_squared = x * x
    x_cubed = x ** 3
    x_fourth = x ** 4
    return x_squared, x_cubed, x_fourth

x_2, x_3, x_4 = my_func(5)
print(x_2, x_3, x_4)


# Python has a math library that support many common functions as well as
# some well known constants.
from math import *

print(pi)

print(e)

print(sqrt(49))

print(log(e * e))

print(log10(1000000))

print(log2(4096))


# The cmath library support working with complex numbers.
from cmath import *

print(sqrt(-1))

print(e ** (1j * pi))

z = 5 + 4j

print(z, z.real, z.imag)


# Lists and working with lists
pets = ['cat', 'dog', 'gerbil', 'hamster']

print(pets)

print(type(pets))

for animal in pets:
    print(animal)


# Indexing into lists
print(pets[0])
print(pets[3])
print(pets[-2])

for n in [0, 1, 2, 3]:
    print('pets[', n, '] = ', pets[n], sep = '')

# The len() function - returns the length of a list
print('The pets list contains', len(pets), 'items')

# lists are mutable - that is, they can be modified
print(pets)
pets[3] = 'snake'
print(pets)

# out-of-range indices make Python unhappy
print(pets[4])
print(pets[-5])

# How can we swap the 6th and 7th values in this list, in a way that will
# work even if we don't know what values are stored there.
xlist = [5, 12, 55, 9, 18, 22, 3, 33]
print(xlist)

# We need to store one of the values in a temporary variable, like this.
temp = xlist[5]
xlist[5] = xlist[6]
xlist[6] = temp
print(xlist)

# Another way is to use multiple assignment, like this
xlist[5], xlist[6] = xlist[6], xlist[5]
