# Scope - what variables have meaning, where?
# example 1
# This works as expected - get_language prints Python
language = 'Python'

def get_language():
    print('This language is called', language)

get_language()

#example 2
# This doesn't work as expected - get_language prints
# Python, but then crashes when it tries to print "3.4"
language = 'Python'

def set_version():
    version = '3.4'

set_version()

def get_language():
    print('This language is called', language)
    print('The version is', version)

get_language()

# The reason for this is that the variable version is
# defined inside the set_version function, and that
# means that the variable version only exists while the
# set_version function is being run. The variable
# langauge, on the other hand, is not defined inside a
# function, and therefore it always exists and is
# always visible everywhere inside the program.


# Local variables - variables defined in a function
def linear(x):
    a = 2.0
    b = 1.0
    print('Inside linear(), a =', a)
    print('Inside linear(), b =', b)
    print('Inside linear(), x =', x)
    return a * x + b

# These are global variables with the same names
a = 9.0
b = 99.0
x = 999.0

print('Before linear(), a =', a)
print('Before linear(), b =', b)
print('Before linear(), x =', x)

result = linear(3.0)
print(result)

print('After linear(), a =', a)
print('After linear(), b =', b)
print('After linear(), x =', x)


# Global variables
# 1st example
# Note that the calculate_tax() function does not
# define a value for the variable tax_rate, yet the
# there is no error. That is because, when a function
# doesn't have its own definition for a variable, it
# looks to seee if the is a global variable with the
# same name. In this case there is, so the calculate_tax
# function uses the global variable tax_rate

# State tax rate
tax_rate = 0.05

# Calculate tax based on price
def calculate_tax(price):
    tax = price * tax_rate
    return tax

cost = 33.0
total_cost = cost + calculate_tax(cost)
print('The total cost is', total_cost)

# 2nd example
# Note that the global tax_rate variable is not defined
# until after the calculate_tax funtion is defined. This
# is not a problem, because we haven't called the
# calculate_tax function yet.

# Calculate tax based on price
def calculate_tax(price):
    tax = price * tax_rate
    return tax

# State tax rate
tax_rate = 0.05

cost = 33.0
total_cost = cost + calculate_tax(cost)
print('The total cost is', total_cost)

# 3rd example
# Now the global tax_rate variable isn't defined until after
# the calculate_tax function is called. This causes an error
# because calculate_tax does't know what value to use for
# the tax_rate

# Calculate tax based on price
def calculate_tax(price):
    tax = price * tax_rate
    return tax

cost = 33.0
total_cost = cost + calculate_tax(cost)

# State tax rate
tax_rate = 0.05

print('The total cost is', total_cost)

# 4th example
# In this example the calculate_tax function has its own
# tax_rate variable. This means that the calculate_tax
# function will not look outside for a global variable named
# tax_cut. But note that the tax_rate variable inside the
# calculate_tax function is a _different_ variable than the
# global tax_rate variable. When the code prints out the
# tax_rate variable at the end, it prints 0.5. That is the
# only tax_rate variable that the print function can see. The
# tax_rate variable in the calculate_tax function only existed
# while the calculate_tax function was running, and even if it
# still existed, it only exists inside the calculate_tax
# function, so the print statement at the end can't see it.

# State tax rate
tax_rate = 0.05

# Calculate tax based on price
def calculate_tax(price):
    #global tax_rate
    tax_rate = 0.06
    tax = price * tax_rate
    return tax

cost = 33.0
total_cost = cost + calculate_tax(cost)
print('The total cost is', total_cost)
print('tax_rate =', tax_rate)


# Looping structures
# While loops
count = int(input('Enter an integer: '))

while count >= 0:
    print(count)
    count = count - 1

# priming the loop
answer = 'yes'

while answer == 'yes':
    x = float(input('Enter a number: '))
    print('The square of', x, 'is', x * x)

    answer = input('Would you like to continue? (yes, no) ')

# Let's try to allow other possible version of 'yes'.
while answer == 'yes' or answer == 'Yes' or answer == 'y' or \
      answer == 'Y':
    x = float(input('Enter a number: '))
    print('The square of', x, 'is', x * x)

    answer = input('Would you like to continue? (yes, no) ')

# Infinite loops - use ctrl-c to stop them
while True:
    print('uh-oh!')


# Collatz conjecture
def collatz(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    print(n)

collatz(-3)
