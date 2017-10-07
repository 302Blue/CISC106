# Last - printing numbers, strings, writing comments,
# using variable
print(2 - 7)

# Printing my name
print("Don't fall asleep")     # name


# Continuing with variables
x = 5
print(x)

x = 12.2
print(x)

y = 77
print(y)

x = y     # Python replaces y with it's value, 77, so the statement becomes
          # x = 77. You don't see this happen, but it's what takes place
          # internally.
print(x)

y = 99    # Changing y at this point does not affect the value of x. x was
          # set to 77, so the value of y has no bearing on the value of x.
print(x)

x = x + 1 # This statements is clearly not mathematically correct, but it
          # is a very important statement that you will use frequently.
          # This statement adds 1 to the current value of x and assigns
          # the result to x. This is called incrementing x. In this case,
          # incrementing by 1.
print(x)

17 = z


# Variable names should be easy to read and meaningful
thisisaterriblvariablename = 1

this_is_a_good_variable_name = 2

thisIAlsoAGoodVariableName = 3

were_LosingGroundA_bit_Here = 4


# Meanginful variable names
monthly_pay_rate = 15.44
average_grade = 91.2
first_nane = 'Preethi'

# Meaningless variable names
a = 15.44
b = 92.1
zz = 'Preethi'


# Variable type (int, float, str)
print(type(1))
print(type(1.0))
print(type('Jon'))

x = type(1)
y = type(1.0)
z = type('Jon')

print(x)
print(y)
print(z)

# Python is dynamically typed - that is, the type of a variable is
# determined by what is stored in the variable. This is much more
# convenient than statically typed languages such as C, C++, and Java
# In these languages you must declare the of type a variable before
# you can use the variable, and the variable must remain that type.
a = 22
print(type(a))
a = 4.143
print(type(a))
a = 'One bright day in the middle of the night...'
print(type(a))


# Reading input from the keyboard
name = input('Enter your name: ')
print('Your name is', name)

age = input('Enter your age: ')
print('Your age is', age)
print("Really? You don't look a day over", age - 5)     # This crashes!

# This is why it crashes:
# input() returns a string, and expressions like theses are meaningless.
'29' - 5
'car' - 5


# Conversion functions
# int()
print(type('29'))
print(type(int('29')))

print(int('29.13'))     # int() fails on strings that look like floats
print(int(29.))
print(int(29.03))
print(int(29.613))
print(int(29.99999999)) # Note that int() truncates the decimal portion.
print(int('car'))       # This fails because 'car' can't be interpreted as
                         # a number

# float()
print(float('17'))
print(float(17))
print(float('16.2342'))

# str()
print(str(88))
print(str(88.))
print(str(88.12345))


# Let's revisit the age problem from earlier
# We now know that we have to convert age to a number.
age = input('Enter your age: ')
print("Really? You don't look a day over", int(age) - 5)

# This is a better approach because age is inherently numeric in
# nature, and this changes age from a string to a number.
age = input('Enter your age: ')
age = int(age)
print("Really? You don't look a day over", age - 5)


# Python math operators
print(2 + 3 * 5 - 4 / 2)
print(2 + 3 * (5 - 4) / 2)
