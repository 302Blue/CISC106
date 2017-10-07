# Using the in operator with if
pets = ['cat', 'dog', 'gerbil', 'hamster', 'rabbit', 'turtle']

pet = input('Enter a type of pet: ')

# Checking if a specific value is in the list
if pet in pets:
    print('Yes, we have a', pet)
else:
    print('No, we don\'t have a', pet)

# The logic can be reversed with "not"
if pet not in pets:
    print('No, we don\'t have a', pet)
else:
    print('Yes, we have a', pet)

# Can use the in operator to test type
x = 7.

#if type(x) == int or type(x) == float:
if type(x) in [int, float]:

    print(x, 'is a number')
else:
    print(x, 'is not a number')

# Can use the in operator to check for valid menu input
choice = 'akjhdas'

if choice in ['a', 's', 'm', 'd', 'e', 'q']:
    print(choice, 'is valid')
else:
    print(choice, 'is not valid')


# Strings
# String are immutable
name = 'Reed'

#name[2] = 'a'     # This causes a runtime error

# This works because it creates a new string instead of modifying the string
name += ' Skillman'
print(name)

# Using for/if with in, with strings
string = 'This is the end'

for char in string:
    print(char)
print()

if '.' in string:
    print('The string contains a period')
else:
    print('The string contains no period.')

# Write a function to check if a string is a vowel
from cisc106_34 import assertEqual

def is_vowel(string):
    if string == 'a' or \
       string == 'e' or \

       
    if string in ['a', 'e', 'i', 'o', 'u']:
    if string in 'aeiou':
        return True
    else:
        return False

assertEqual(is_vowel('a'), True)
assertEqual(is_vowel('b'), False)
assertEqual(is_vowel('iou'), False)


# String methods - note that, unlike list methods, string methods typically
# return a new string.
string = '00fd9sdf0'
print(string)
print('isalnum =', string.isalnum())

string = '   \t\n\n   \t . '
print('isspace =', string.isspace())

string = 'ABC, 123, Do Re Mi'
print(string.lower())

string = string.lower()
print(string)

print(pets)
pets.reverse()     # This list method directly modifies pets
print(pets)


# Write a function to count the vowels in a string
def count_vowels(string):
    count = 0
    for char in string:
        if is_vowel(char):
            count += 1

    print(string, 'has', count, 'vowels')

count_vowels('This is the end')
count_vowels('Mississippi')


# Modify the function to also output each vowel and its index.
def count_vowels(string):
    count = 0
    #for char in string:
    for i in range(len(string)):
        if is_vowel(string[i]):
            count += 1
            print(string[i], 'is at index', i)

    print(string, 'has', count, 'vowels')

count_vowels('This is the end')
count_vowels('Mississippi')


# Write a function to find and print the 3rd word in a string of words.
def pluck_word3(string):
    i = 0

    for word in range(3):
        # Note we check i here to avoid running off the string.
        while i < len(string) and string[i].isspace():
            i = i + 1

        start = i
        
        # Note we check i here to avoid running off the string.
        while i < len(string) and not string[i].isspace():
            i = i + 1

        stop = i

    print(string[start:stop])

pluck_word3('   This is    the')
