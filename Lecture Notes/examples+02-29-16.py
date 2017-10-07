# Program Testing - use convert_F_to_C as an example
# Manual testing
from cisc106_34 import assertEqual

def convert_F_to_C(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius

print('-40 °F is', convert_F_to_C(-40), '°C')
print('32 °F is', convert_F_to_C(32), '°C')
print('212 °F is', convert_F_to_C(212), '°C')

# Testing using assertEqual()
from cisc106_34 import assertEqual

def convert_F_to_C(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius

assertEqual(convert_F_to_C(-40), -40)
assertEqual(convert_F_to_C(32), 0)
assertEqual(convert_F_to_C(212), 100)
assertEqual(convert_F_to_C(41), 6)     # example of a failure

# What about rounding?
assertEqual(convert_F_to_C(75), 23.88888888888889)

# Use round() function
print(2 / 3)
print(round(2 / 3, 2))
print(round(2 / 3, 4))
print(round(2 / 3, 12))

# Using round() with assertEqual()
assertEqual(round(convert_F_to_C(75), 2), 23.89)


# Documentation - the Python Doc String
def convert_F_to_C(fahrenheit):
    '''
    Convert temperature from °F to °C
    Parameters:
        fahrenheit (number) - temperature in °F
    Returns:
        celsius (float) - converted temperature in °C
    '''
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius

# Accessing the doc string
help(convert_F_to_C)
print(convert_F_to_C.__doc__)


# Puzzle - write a function to reverse the digits of a 2-digit number
def reverse_digits(number):
    '''
    Reverse the digits of a 2 digit number
    Parameters:
        number (int) - original number
    Returns:
        rebmun (int) - reversed number
    '''
    ones_digit = number % 10
    tens_digit = number // 10
    rebmun = ones_digit * 10 + tens_digit
    return rebmun

print('The reverse of 37 is', reverse_digits(37))

# Now test with assertEqual()
assertEqual(reverse_digits(37), 73)
assertEqual(reverse_digits(2), 20)
assertEqual(reverse_digits(90), 9)
assertEqual(reverse_digits(0), 0)

# What happens if the argument is negative? Does it work?
assertEqual(reverse_digits(-93), -39)


# Flow of Control
# The if statement
if 15 < 8:
    print('It\'s true')
    
print('Continue processing here...')

# Another example
age = int(input('How old are you? '))
if age < 21:
    print('I\'m sorry, but I can\'t serve you.')

print('Continue processing here...')

# The if-else statement
age = int(input('How old are you? '))
if age < 21:
    print('I\'m sorry, but I can\'t serve you.')
else:
    print('What would you like to drink?')

print('Continue processing here...')

# Write a function can_vote() that takes a person's age and returns 'yes'
# or 'no' depending on whether or not the person is old enough to vote
def can_vote(age):
    if age < 18:
        return 'no'
    else:
        return 'yes'

# Here are 3 variations on this function. None of them is the "correct"
# approach. They are all similar and valid. The point is to be aware that
# there are many ways to accomplish the same goal.
def can_vote(age):
    if age < 18:
        decision = 'no'
    else:
        decision = 'yes'

    return decision

def can_vote(age):
    decision = 'yes'
    
    if age < 18:
        decision = 'no'

    return decision

def can_vote(age):
    if age < 18:
        return 'no'

    return 'yes'

answer = can_vote(17)
print(answer)
