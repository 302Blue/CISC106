# Creating a pie chart
import matplotlib.pyplot as plt

data = [20, 26, 17, 6, 5]
plt.title('Matplotlib Pie Chart')
plt.pie(data)
plt.show()


# recursive n! function
def factorial(n):
    # check for the base case
    if n == 0:
        return 1

    # handle the recursive case
    return n * factorial(n - 1)

k = 10
print(k, '! = ', factorial(k), sep = '')

# Fibonacci sequence
def fibonacci(n):
    # check for the base case
    if n == 1:
        return 1
    elif n == 0:
        return 0

    # handle recursive case
    #F(n) = F(n - 1) + F(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Output a list of the 1st 10 Fibonacci numbers
for n in range(10):
    print('F(', n, ') = ', fibonacci(n), sep = '')

# 2-dimensional lists
my_list = [99, ['a', [6, 16, 3], 4.44], [True, ['1', 'b']], 'k']

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print()
print(my_list[1][0])
print(my_list[1][1])
print(my_list[1][2])
print()
print(my_list[1][1][0])
print(my_list[1][1][1])
print(my_list[1][1][2])

# Database containing 6 book records
books = [['Ant and Bee', 'Angela Banner', 1950, 'AB24'],
         ['Dice', 'Ricky Jay', 2003, '51502713'],
         ['Flatland', 'Edwin Abbott Abbott', 1880, 'EA91'],
         ['naked', 'David Sedaris', 1997, 'DS132'],
         ['The Great Bridge', 'David McCullough', 1972, 'TG25.N53 M32'],
         ['The TEXbook', 'Donald Knuth', 1984, '9322854']]

# Accessing book records, and fields in those records
print(books[2])
print(books[5])
print()
print(books[4][0])
print(books[0][3])

# Using global variables for field names
# This make the code easier to read and easier to update
TITLE = 0
AUTHOR = 1
YEAR = 2
CALL = 3

print(books[4][TITLE])
print(books[0][CALL])

# What if we add a location field to the database?
books = [['Hockessin', 'Ant and Bee', 'Angela Banner', 1950, 'AB24'],
         ['Newark', 'Dice', 'Ricky Jay', 2003, '51502713'],
         ['Wilmington', 'Flatland', 'Edwin Abbott Abbott', 1880, 'EA91'],
         ['Morris', 'naked', 'David Sedaris', 1997, 'DS132'],
         ['Morris', 'The Great Bridge', 'David McCullough', 1972, 'TG25.N53 M32'],
         ['Morris', 'The TEXbook', 'Donald Knuth', 1984, '9322854']]

# These indices have to be updated throughout the program
print(books[4][0])
print(books[0][3])

# Updating the global constants is much simpler
LOCATION = 0
TITLE = 1
AUTHOR = 2
YEAR = 3
CALL = 4

print(books[4][TITLE])
print(books[0][CALL])
print(books[3][LOCATION])


# Read in a file containing dog database info, create a database, and
# print it out.
# Global constants for field names
NAME = 0
BREED = 1
AGE = 2
WEIGHT = 3

filename = input('Enter name of dog file: ')

dog_file = open(filename, 'r')

dog_db = []

for line in dog_file:                # Read the file line-by-line
    dog_record = line.split(',')     # Turn line into a dog record
    dog_record[AGE] = int(dog_record[AGE])           # Correct data type
    dog_record[WEIGHT] = float(dog_record[WEIGHT])   # Correct data type
    dog_db.append(dog_record)        # Add record to the database

dog_file.close()

for dog in dog_db:
    print(dog)

# global database
dog_db = []

# put this code in a function
def initialize_dog_db():
    filename = input('Enter name of dog file: ')

    dog_file = open(filename, 'r')

    for line in dog_file:
        dog_record = line.split(',')
        dog_record[AGE] = int(dog_record[AGE])
        dog_record[WEIGHT] = float(dog_record[WEIGHT])
        dog_db.append(dog_record)
        #dog_db = dog_db + [dog_record]     # This won't work with a global
                                            # dog_db

    dog_file.close()

    return

def main():
    initialize_dog_db()

    print('The database contains the following breeds:')
    for dog in dog_db:
        print(dog[BREED])

main()
