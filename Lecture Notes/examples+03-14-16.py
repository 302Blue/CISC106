# for loops with lists (from last time)
for value in [1, 2, 3, 4, 5]:
    print(value)

for field in ['Thomas', 'Smith', 'cisc456', 'B+', 'senior']:
    print(field, '\t', sep = '', end = '')


# Generate a conversion table from °F to °C, using a for loop with a list
from menu_functions import convert_F_to_C

print('\n Temperature')
print('Conversion Table')
print('  °F        °C')
print('----------------')

for temp_f in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    temp_c = convert_F_to_C(temp_f)
    print('', format(temp_f, '3d'), '   ', format(temp_c, '6.1f'))


# The range() function - stop value is NOT included in resulting list!
print(list(range(1, 6, 1)))
print(list(range(1, 6)))
print(list(range(5)))
print(list(range(3, -10, -3)))
print(list(range(3, -10, 3)))     # This creates an empty list - why?


# for loops with range() functions
for n in [1, 2, 3, 4, 5]:
    print(n)

for n in range(1, 6, 1):
    print(n)

for n in range(5):
    print(n)

# Recreate conversion table using a for loop with the range() function
from menu_functions import convert_F_to_C

print('\n Temperature')
print('Conversion Table')
print('  °F        °C')
print('----------------')

#for temp_f in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
for temp_f in range(0, 101, 10):
    temp_c = convert_F_to_C(temp_f)
    print('', format(temp_f, '3d'), '   ', format(temp_c, '6.1f'))

# Simple puzzle - write code to display the sum of 100, 105 and 110
print(100 + 105 + 110)

# More difficult puzzle - write code to diplay the sum of all the
# numbers from 100 to 500000, in steps of 5.
# Problems of this sort often use an accumulator to add up all the
# numbers.
total = 0     # total is an ccumulator

for x in range(100, 500001, 5):
    total = total + x

print(format(total, ',d'))

# Here's the same solution except that it uses a while loop.
k = 100
total = 0

while k <= 500000:
    total = total + k
    k = k + 5

print(format(total, ',d'))


# Hard problem - A child saves 1 penny on the 1st day, 2 on the 2nd day,
# 4 on the 3rd day, 8 on the 4th day, etc. How many pennies does the child
# have after 30 days?
total = 0     # accumulator

for day in range(0, 30):
    total = total + 2 ** day

print('Total = $', format(total/100, ',.2f'), sep = '')


# for loop - while loop equivalence
# Here's our original solutino to the penny saving problem
total = 0

for day in range(0, 30):
    total = total + 2 ** day

print('Total = $', format(total/100, ',.2f'), sep = '')

# Here's a while loop version of the same solution
total = 0

day = 0
while day < 30:
    total = total + 2 ** day
    day = day + 1

print('Total = $', format(total/100, ',.2f'), sep = '')
