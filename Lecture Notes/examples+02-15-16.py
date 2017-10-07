# Review from last time
number = input('How many apples? ')
number = int(number)
print('Once more apple would be', number + 1)


# Conversion functions int(), float(), and str()
num = '12'
print(num)

# Note that int() doesn't change num!
print(int(num))
print(type(num))

# You need to set num equal to int(num) if you want to change num
num = int(num)
print(num)
print(type(num))

# float() behaves the same way
print(float(num))
print(type(num))

num = float(num)
print(num)
print(type(num))


# Operator precedence and associativity
print(2 + 3 * 5 - 4 / 2)
print(2 + 3 * (5 - 4) / 2)
print(2 + 3**2 * 5 - 4 / 2)
print((2 + 3)**2 * 5 - 4 / 2)

# left to right associativity for all but **
print(1 + 2 + 3 + 4 + 5)

# This evaluate 3 ** 4 first
print(2 ** 3 ** 4)

print(2 ** (3 ** 4))     # This is the same as the default behavior
print((2 ** 3) ** 4)     # This changes the order of evaluation

# The / and // operators
# The division operator - this is what you expect from division
print(4 / 3)      #  1.333333333333333
print(-4 / 3)     # -1.333333333333333

# floor division - //
# This operator rounds down to the nearest integer - it round
# down towards -∞, not towards 0.
print(4 // 3)     #  1
print(-4 // 3)    # -2

# modulo operator (remainder) - %
# This operator give you the remainder when dividing the
# first number by the second
print(5 % 2)           # 1
print(5 % 3)           # 2
print(7 % 1)           # Anything mod 1 is 0
print(3 % 3)           # Anything mod itself is 0
print(8.75 % 2.5)      # This also works with decimals

# Unexpected behavior for % with negative numbers
# You need to be aware of this, but I won't test you on it.
print( 5 %  3)
print( 5 % -3)
print(-5 %  3)
print(-5 % -3)


# Type conversion (implicit, coercion)
# If both operands are ints, the result is an int. If even one
# operand is a float, the other is converted to a float and the
# result is a float
print(1 + 2)
print(type(1 + 2))

print(1. + 2)
print(type(1. + 2))

print(1 + 2.)
print(type(1 + 2.))

print(1. + 2.)
print(type(1. + 2.))

print(1. - 2)
print(type(1. - 2))

print(1. * 2)
print(type(1. * 2))

print(1. // 2)
print(type(1. // 2))

print(1. % 2)
print(type(1. % 2))

print(1. ** 2)
print(type(1. ** 2))

# The one exception is float division (/), which _always_
# returns a float.
print(1 / 2)
print(type(1 / 2))


# Formatting number with format()
# Here is the default output for varioius floats
fraction = 5 / 3
print(fraction)
print(1.0)
print(1.000000000000)

# floating point format
print(format(fraction, 'f'))
print(format(fraction, '.3f'))
print(format(12344 + fraction, '.3f'))
print(format(12344 + fraction, '15.3f'))
print(format(12344 + fraction, '5.3f'))
print(format(12344 + fraction, '15,.3f'))
