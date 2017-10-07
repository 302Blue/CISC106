# Function returns values, and None and NoneType
def my_function():
    print('Hello')
    #return 5   # this returns the value 5
    #return     # return without a value causes the function to return None
                # not using return at all also causes function to return None

x = my_function()
print('x =', x)
print(type(x))

# The key point is that EVERY python function returns a value. If you don't
# specify the value to be returned, the function will return None - even if
# you don't use the return statement at all!

# Note that None is type NoneType, which is a new variable type! It is
# unusual in that the only NoneType value is None.


# Continuing from last time
from cisc106_34 import assertEqual

def can_vote(age):
    if age < 18:
        decision = 'no'
    else:
        decision = 'yes'

    return decision

# Note that the fact that these assertEqual() tests succeed indicates that it
# is possible to compare strings.
assertEqual(can_vote(17), 'no')
assertEqual(can_vote(21), 'yes')
assertEqual(can_vote(18), 'yes')


# Strings are compared letter by letter just like comparing words to put them
# in alphabetical order. Each character has a numerical value associated with
# which is used to do the comparison. The values are assigned so that you get
# the expected result - a < b < c < ... < z, and similarly A < B < C < ... < Z.
# However, note that all uppercase letters are less than every lower case
# letter - Z < a. Also, every digit is lower than every letter - 9 < A.
name_1 = 'Mohan'
name_2 = 'Morgan'     # Change to Martin and output order changes. Note that
                       # using martin rather than martin results in Mohan
                       # being printed first because M < m.

if name_1 < name_2:
    print(name_1)
    print(name_2)
else:
    print(name_2)
    print(name_1)

# Be careful comparing numbers as string
if '16' < '106':
    print('I though so')
else:
    print('What?!!')

# To compare numbers as strings you need to ensure that the have the same
# number of digits, so comparing '016' to '106' will give the expected
# result.


# Boolean variables (True, False)
print(5 < 8)
print(type(5 < 8))     # True and False are type bool - a new variable type!
                        # True and False are the _only_ bool variables

# Compound Boolean expressions (using and, or and not)
over_18 = True
signed_waiver = True

if over_18 and signed_waiver:
    print('Permitted on extreme ride')
else:
    print('Not permitted on extreme ride')

# slightly more complex example
over_18 = True
with_parent = True
signed_waiver = False

# This give unexpected retuts because and is higher precedence than or
if over_18 or with_parent and signed_waiver:
    print('Permitted on extreme ride')
else:
    print('Not permitted on extreme ride')

# Using parentheses we can force the or to be evaluated first
if (over_18 or with_parent) and signed_waiver:
    print('Permitted on extreme ride')
else:
    print('Not permitted on extreme ride')


# Examples of left-to-right associativity of 'and' and 'or'
a = True
b = True
c = True
d = False
#print(a and b and c and not d)

print(not a or not b or not c or d)


# Does this behave as expected? It does not!
x = 1     # Try 1, 2, 3, 4, and 6

if x == (2 or 4 or 6):     # <-- Don't try shortcuts like this
    print('x is 2, 4, or 6')
else:
    print('x is not 2, 4, or 6')

# We need to correct the compound boolean expression
x = 1     # Try 1, 2, 3, 4, and 6

if x == 2 or x == 4 or x == 6:     # <-- Instead, do this
    print('x is 2, 4, or 6')
else:
    print('x is not 2, 4, or 6')


# Review if/if-else statements
age = int(input('How old are you? '))
if age < 21:
    print('I\'m sorry, but I can\'t serve you.')
else:
    print('What would you like to drink?')

print('Continue processing here...')


# if-elif-elif-...-elif-else
score = float(input('Enter score: '))

if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is an B')
elif score >= 70:
    print('Your grade is an C')
elif score >= 60:
    print('Your grade is an D')
else:
    print('Your grade is an F')

# With an if-elif-... once a if or elif clause if found to be True, the
# statements in it's body are executed and the rest of the if-elif-...
# is skipped.

# What about this approach? Doesn't work
if score >= 90:
    print('Your grade is an A')
if score >= 80:
    print('Your grade is an B')
if score >= 70:
    print('Your grade is an C')
if score >= 60:
    print('Your grade is an D')
else:
    print('Your grade is an F')

# With a series of if statements, every if statement will be evaluated


# How do you round a float to the nearest int?
# Remember that int() truncates decimal portions
print(int(4.2))
print(int(4.9))

# Add 0.5 before converting to int
print(int(5.3 + 0.5))       # This rounds down
print(int(5.999 + 0.5))     # This rounds up
print(int(5.5 + 0.5))       # This rounds up
print(int(5.4999999 + 0.5)) # This rounds down
