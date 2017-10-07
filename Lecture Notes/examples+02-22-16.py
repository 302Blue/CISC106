# From last time - using end and sep with print()
print(1, 2, 3, sep = ', ')

# Escape sequences - \n, \t, \', \", \\
print('Don\'t fall asleep')

# Escaping the escape character - \\
# The first print() statement has a problem because the backslash at the
# end of the line is being combined with the final quote mark to make a
# Python escape sequence. This means that the final quote mark does not
# end the string. Notice that the parnethesis at the end of the line is
# green, indicating that Python thinks it part of the string.
print('Python is located in C:\Python\')

# By escaping the final backslash we arte telling Python to simply print
# the backslash rather than treat it as part of an escape sequence. Note
# that the final parenthesis is now black.
print('Python is located in C:\Python\\')


# How to document your code for Lab 1.
# Here are some examples of comments that describe what the convert_F_to_C()
# function does. Note that they don't say anything about how they do what
# they do - only what they do.
      
# This program asks the user for a temperature in °F and
# outputs the equivalent temperature in °C.

# This program converts temperature from °F to °C, and outputs
# the result.

# Convert temperature from °F to °C and output result
fahrenheit = float(input('Enter temperature in °F: '))
# Calculate °C from °F
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
# Output result
print(fahrenheit, '°F converts to', celsius, '°C')

# Ask user for two grades and output the average
grade1 = float(input('Enter 1st grade: '))
grade2 = float(input('Enter 2nd grade: '))
average = (grade1 + grade2) / 2.0
print('The average grade is', average)


# Errors (syntax, semantic/logic, runtime)
# syntax error
3 75
4 *** 3
result 12
print('The result is' 5)
num = float(input('Enter number: ')
