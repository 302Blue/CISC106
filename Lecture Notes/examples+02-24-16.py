# Errors (syntax, semantic/logic, runtime)
# syntax error
3 75                                  # missing decimal point?
4 *** 3                               # extra '*'?
result 12                             # missing '='?
print('The result is' 5)              # missing comma
num = float(input('Enter number: ')   # missing ')'

# semantic errors (errors in logic or meaning
print(x)                              # x is not defined
x = x + 1                             # x is not defined

x = int(input('Enter number: '))
print('Double your number is', x + 2) # Maybe x * 2?
            
divisor = float(input('Enter divisor: '))
print('10 divided by', divisor, '=', 10 / divisor) # problem if divisor = 0

# runtime error - any error that causes a program to stop
print(x)
x = x + 1

z = 5 + 'cat'


# Writing Functions
# Suppose we need to write these lines of code  many times over in our
# program.
print('*************')
print('* IMPORTANT *')
print('*************')

# Instead of typing the same lines again and again, we can put the lines
# in a function, and simplpy call the function whenever we need those
# lines of code to run.
            
# Here's the same set of statments, but in a function now
def important():
    print('*************')
    print('* IMPORTANT *')
    print('*************')

# You have to call the function to get the function statements to execute.
important()


# Rewrite the temperature conversion program as a function
fahrenheit = float(input('Enter a temp in °F: '))
celsius = (fahrenheit - 32.0) * 5.0 /9.0
print(fahrenheit, '°F is equal to', celsius, '°C')

def convert_F_to_C():
    fahrenheit = float(input('Enter a temp in °F: '))
    celsius = (fahrenheit - 32.0) * 5.0 /9.0
    print(fahrenheit, '°F is equal to', celsius, '°C')

convert_F_to_C()

# Using parameters
# Let's add a parameter to the function
def convert_F_to_C(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 /9.0
    print(fahrenheit, '°F is equal to', celsius, '°C')

# Now when we call the function we have to provide an argument - a value
# that will be assigned to the parameter.
convert_F_to_C(212)

# We can replicate the original behavior
fahrenheit = float(input('Enter a temp in °F: '))
convert_F_to_C(fahrenheit)

# Returning a value - using the return statement
# This function does not generate any output. Instead it returns the
# value of celsius.
def convert_F_to_C(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 /9.0
    return celsius

# We can save the returned value in the variable result, and print it.
result = convert_F_to_C(32)
print('32 °F is', result, '°C')

# We can also replicate the behavior of the original function, but now
# we have to ask for the input and diplay the output because the function
# no longer peroforms either of those tasks.
degrees_f = float(input('Enter a temp in °F: '))
degrees_c = convert_F_to_C(degrees_f)
print(degrees_f, '°F is equal to', degrees_c, '°C')

# Important concept - what do we mean when we say that the function
# call is replaced by the return value?
print(float(input('Enter number: ')))

print(float('12345'))

print(12345.0)

# Here is our grade averaging program
grade1 = float(input('Enter 1st grade: '))
grade2 = float(input('Enter 2nd grade: '))
average = (grade1 + grade2) / 2.0
print('The average grade is', average)

# Let's convert this to a function
def average_grade():
    grade1 = float(input('Enter 1st grade: '))
    grade2 = float(input('Enter 2nd grade: '))
    average = (grade1 + grade2) / 2.0
    print('The average grade is', average)

average_grade()

# Now let's modify the function so that it no longer asks the user to
# input the grades, and instead it expects that two grades to be
# provided through two parameters.
def average_grade(grade1, grade2):
    average = (grade1 + grade2) / 2.0
    print('The average grade is', average)

average_grade(80, 100)


# Puzzle - write a functino to calculate the gravitational force between
# two masses.
# Function to calculate the force of gravity
def gravity(mass1, mass2, radius):
    G = 6.673e-11
    force = G * mass1 * mass2 / radius ** 2
    return force

# Let's try our function with the sun and the earth
earth = 5.972e24     # mass of earth in kg
sun = 1.989e30       # mass of sun in kg
distance = 1.5e11    # distance between the centers of the earth and sun

force_earth_sun = gravity(earth, sun, distance)
newtons_per_pound = 4.45     # conversion factor from lbs to kg
force_earth_sun = force_earth_sun / newtons_per_pound

print('The gravitational force between the earth and the sun is',
      format(force_earth_sun, ',.0f'), 'pounds')

# Let's try again with two 150 lb people, 1 meter apart.
force_2_people = gravity(150 * 4.45, 150 * 4.45, 1)
print(format(force_2_people / 4.45, '.6e'))


# Importing from libraries
import math
print(math.sqrt(49)) # log, log10, sin, cos, tan, pi

from math import sqrt
print(sqrt(49))
