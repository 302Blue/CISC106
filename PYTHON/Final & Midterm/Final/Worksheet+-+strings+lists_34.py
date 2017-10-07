# Worksheet on strings, lists

# String slices
# What is the output of the following statements?

x = 'mnopqrstuv'
print(x)
print(x[1])
print(x[1:2])
print(x[1:2:1])
print(x[1:5:1])
print(x[1:6:2])
print(x[0::2])
print(x[::2])
print(x[5:])
print(x[:5])
print(x[:6:])

# Using the "in" operator with strings and lists
# What is printed?
food = 'marshmallow'

for i in food:
    print(i)

#What is printed?	
for i in range(len(food)):
    print(food[i])
	
#What is printed?  What does x represent semantically?
x = 0
for i in food:
    if i == 'm':
        x = x + 1
print(x)


#What does the following function do?  Does it remind you of anything?
def convert(remainder):
    Table = '0123456789ABCDEF'
    if 0 <= remainder <= 15:
        return Table[remainder]
    else:
        return None
	
	

#What is printed?
fruits = ['apple', 'pear', 'orange', 'banana', 'tomato', 'melon']
for x in fruits:
    for i in x:
        if i == 'a':
            print(i)
			

#What is printed?			
fruits = ['apple', 'pear', 'orange', 'banana', 'tomato', 'melon']
for x in fruits:
    for i in x:
        if i == 'a':
            print(x)
			
			
#Given a list of first names:
#  e.g., names = ['Sam', 'Steve', 'Ann', ..., 'Sue']

# Write code that will print out all names that contain the letter 's'.

# Write code that will print out the number of names that contain the
# letter 's'.

# Write code that will print out the total number of times the letter
# 's' occurs in all of the names.
