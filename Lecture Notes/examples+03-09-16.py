# Collatz conjecture
def collatz(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    print(n)

# Input testing - interacting with the user to force them to
# enter valid input.
# Here we use a while loop to force the user to enter valid input
n = int(input('Enter a positive integer: '))

while n < 1:
    print(n, 'is not a positive integer.')
    n = int(input('Enter a positive integer: '))

collatz(n)

# another example
# Here we use a while loop to force the user to input either yes
# or no.
answer = 'yes'

while answer == 'yes':
    x = float(input('Enter a number: '))
    print('The square of', x, 'is', x * x)

    answer = input('Do you want to continue (yes, no)? ')
    # Note the use of "and" in this expression. When first
    # learning to write boolean expressions, many students
    # use "or" instead of "and", but that causes everything
    # to be considered invalid input. Try to understand why?
    while answer != 'yes' and answer != 'no':
        print('Please answer yes or no')
        answer = input('Do you want to continue (yes, no)? ')

# Sometimes it is difficult to create a boolean expression that
# will select invalid input. An alternative is to write a
# boolean expression that selects valid input, enclose it in
# parnetheses and put "not" in front of it.
    while not (answer == 'yes' or answer == 'no'):
        print('Please answer yes or no')
        answer = input('Do you want to continue (yes, no)? ')


# Heron's triangle formula
def heron(a, b, c):
    x = (a + b + c)/ 2.0
    area = (x * (x - a) * (x - b) * (x - c)) ** 0.5
    return area

print('Area =', heron(3, 4, 5))
print('Area =', heron(5, 12, 13))
print('Area =', heron(5, 7, 13))

# Add input testing to ensure all sides are positive
x = float(input('Length of 1st side: '))
while x <= 0:
    print('side length must be positive.')
    x = float(input('Length of 1st side: '))
    
y = float(input('Length of 1st side: '))
while y <= 0:
    print('side length must be positive.')
    y = float(input('Length of 2nd side: '))

z = float(input('Length of 1st side: '))
while z <= 0:
    print('side length must be positive.')
    z = float(input('Length of 3rd side: '))

# Now check that the sides form a valid triangle
if x + y <= z:
    print('Invalid triangle')
elif y + z <= x:
    print('Invalid triangle')
elif z + x <= y:
    print('Invalid triangle')
else:
    print('Area =', heron(x, y, z))


# Parameter testing - like input testing except that there is
# no interaction with a user. Function often do this to ensure
# that they are given valid input. They typically return a
# special value, like None, to indicate that the input was
# invalid.

# Heron's triangle formula with parameter testing
def heron(a, b, c):
##    if a <= 0:
##        return None
##    if b <= 0:
##        return None
##    if c <= 0:
##        return None

    # The is the same test as above, but consolidated into a
    # single boolean expression
    if a <= 0 or b <= 0 or c<= 0:
        return None

    if a + b <= c or b + c <= a or c + a <= b:
        return None

    x = (a + b + c)/ 2.0
    area = (x * (x - a) * (x - b) * (x - c)) ** 0.5
    return area

area = heron(3, 4, 15)

# We need to check for the special value the indicates that the
# input was invalid.
if area == None:
    print('Invalid triangle')
else:
    print('Area =', area)


# Menu driven programming
from menu_functions import *

def menu():
    print()
    print('Please choose from the following options:')
    print('    c - convert temperature from °F to °C')
    print('    h - area of a triangle using Heron\s formula')
    print('    r - reverse a two digit number')
    print('    q - quit')

def main():
    menu()
    choice = input('Enter your choice')

    # This while loop controls the user's interaction with the menu
    while choice != 'q':
        if choice == 'c':
            temp_f = float(input('Input temp in °F: '))
            print(convert_F_to_C(temp_f))
        elif choice == 'h':
            x = float(input('Length of 1st side: '))
            y = float(input('Length of 2nd side: '))
            z = float(input('Length of 3rd side: '))
            print(heron(x, y, z))
        elif choice == 'r':
            number = int(input('Enter a 2-digit number: '))
            print(reverse_digits(number))
        else:
            print('Invalid menu choice. Try again')

        # After handling the user's previous menu choice
        # request a new choice before repeating the loop.
        menu()
        choice = input('Enter your choice')

main()

# For loops
# Examples of lists - a comma separated list of values enclosed
# in square brackets
print([1, 2, 3, 4, 5])
print([1, 'two', 3.456, False, None])

x = [1, 2, 3, 4, 5]
y = [1, 'two', 3.456, False, None]

print(x)
print(y)


# for loop examples with lists
for value in [1, 2, 3, 4, 5]:
    print(value)
