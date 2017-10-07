# Formatting numbers with format()
fraction = 5 / 3
print(fraction)
print(format(fraction, 'f'))
print(format(fraction, '.2f'))
print(format(12344 + fraction, ',.2f'))

# exponential format (scientific notation)
print(format(12344 + fraction, 'e'))
print(format(12344 + fraction, '.2e'))
print(format(12344 + fraction, '20.2e'))
print(format(12344 + fraction, '2.2e'))

# percentage format
print(format(fraction, '%'))
print(format(fraction, '.3%'))
print(format(12344 + fraction, ',.3%'))
print(format(12344 + fraction, '20,.3%'))

# integer format
print(9189)
print(format(9189, 'd'))
print(format(9189, '8d'))
print(format(9189, '8,d'))

# What does format() actually do?
# format doesn't change the value!
print(fraction)
format(fraction, '.2f')
print(fraction)

# format creates a string!
print(type(format(fraction, '.2f')))

# Don't do this - it changes fraction from a number to a string
# and it reduces to precision of the number by eliminating
# some decimal places.
fraction = format(fraction, '.2f')
print(fraction)


# More about the print() function
# end-of-line-string - by default it is the "return" key
print(1)
print(2)
print(3)

# Here we set it to the empty string - in other words, nothing
print(1, end = '')
print(2, end = '')
print(3)

# Here we set it to a long string
print(1, end = '-python 3.4-')
print(2, end = '-python 3.4-')
print(3)

# item-separator - by default this is a space
# Note that the spacing used to write the statement has no
# bearing on th spacing used in outputting the values
print(1, 2, 3)
print(1,2,3)
print(1,                    2,            3)

# Let's change the item separator and look at the results
print(1, 2, 3, sep = '')
print(1, 2, 3, sep = '0000')

# Why doesn't this line output an asterisk? Because only one
# item is printing, so there is nothing to separate
print(1, sep = '*')

# Multi-line statements
# Use a backslash at the end of a line to tell Python that
# the next line is a continuation of the current line
total_energy = 0.5 * mass_1 * velocity_1 ** 2 + \
               mass_1 * g * height_1 + \
               0.5 * mass_2 * velocity_2 ** 2 + \
               mass_2 * g * height_2 + \
               0.5 * mass_3 * velocity_3 ** 2 + \
               mass_3 * g * height_3

# Here is a way to avoid using very long lines.
e1 = 0.5 * mass_1 * velocity_1 ** 2 + mass_1 * g * height_1
e2 = 0.5 * mass_1 * velocity_1 ** 2 + mass_1 * g * height_1
e3 = 0.5 * mass_1 * velocity_1 ** 2 + mass_1 * g * height_1
total_energy = e1 + e2 + e2

# Note that the backslash at the end of the first line is
# green, indication that Python thinks it's part of the
# string - it is _not_ a continuation character because it
# is in the string. In this case the output includes a lot
# of extra space between fathers and brought, which is not
# what we want.
print('Four score and seven years ago our fathers \
       brought forth on this continent...')

# Instead, break the string into multiple pieces like this
# and use a line continuation character at the end of the
# first line.
print('Four score and seven years ago our fathers', \
      'brought forth on this continent...')

# Actually, if the code you want to continue is inside of a
# set of parentheses, no line continuation character is
# needed.
print('The contents of this box are', num1,
      'apples, and', num2, 'oranges')


# Strings operations
# concatenation (string addition)
# Note that no space is included between the strings - this
# is not the same as the print statement.
print('Hello' + 'World')

# We can add a space in any of the following ways.
print('Hello' + ' ' + 'World')
print('Hello' + ' World')
print('Hello ' + 'World')

# Here's a more extreme example
Style = 'S' + 't' + 'y' + 'l' + 'e'
print(Style)

# Here's an example using variables rather than explicit
# strings.
first = 'Jon'
last = 'Leighton'
print(first, last)
full = first + ' ' + last
print(full)

# string repitition (string multiplication)
atmark = '@'
print(atmark)

# This repeats the value of atmark 5 times.
print(atmark * 5)

# Here's a more complex pattern using both conatenation and
# repitition
pattern = atmark * 5 + '$' * 3
print(pattern * 7)


# Escape sequences - how to output special characters
# newline character
print(1, end = '')
print(2, end = '')
print(3)

# This actually sets the end-of-line string to its default
# value
print(1, end = '\n')
print(2, end = '\n')
print(3)

# This example produces double spaced output
print(1, end = '\n\n')
print(2, end = '\n\n')
print(3)

# tab character
print('1234')
print('1\t2\t3\t4')

# escaping ' and "
print("Don't use a contraction")
print('Don\'t use a contraction')
