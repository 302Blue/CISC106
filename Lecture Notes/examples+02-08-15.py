# When running a script, Python generates no output unless explicitly
# directed to generate output. The following 4 lines of code generate
# no output.
5
2 - 7
8 * 1.3 / 0.1 + 2 ** 3
'Jon'

# The print statement generates output on the screen.
print(5)
print(2 - 7)
print(8 * 1.3 / 0.1 + 2 ** 3)

# Python allows you to identify text with either single quotes or double
# quotes. Using one style to identify your text allows you to use the
# other style as part of the text.
print("Jon")

print('I "like" programming')

print("I don't like programming")

print('Jon','Leighton')

print('The number of millimeters in a centimeter is', 10)

print('There are', 12, 'eggs in a dozen')

# Comments
# Print my UD address information
# Here is where I use the print() function to print out my name and
# address information - this is an excessive comment
print('Jon Leighton')     # name   (inline comment)
print('Room 413')         # room
print('Smith Hall')       # building


# Variables

# text
name = 'Jon Leighton'
print(name)     # This prints the value stored in the variable name
print('name')   # This print the text 'name'

# numbers
x = 5
print(x)

x = 12.2        # We can change the value stored in x
print(x)

y = 77
print(y)

x = y           # We can set x to the value stored in y
print(x)
