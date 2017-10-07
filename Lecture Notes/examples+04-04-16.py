# Review - lists
pets = ['cat', 'dog', 'gerbil', 'hamster']

print(pets)
print(pets[0], pets[3])

pets[2] = 'snake'
print(pets)

#print(pets[5])     # out-of-range index causes a crash
#print(pets[-5])    # out-of-range index causes a crash

pets_len = len(pets)
print('The pets list contains', pets_len, 'items')


# Two ways to loop over lists
# Example 1: searching for an item in a list
pets = ['cat', 'dog', 'gerbil', 'snake', 'hamster', 'zebra']
zebra = False

# Looping directly over the list. The values in the list are assigned to
# the loop variable.
for animal in pets:
    if animal == 'zebra':
        zebra = True

if zebra:
    print('Yes, we have a zebra.')
else:
    print('No, we don\'t have a zebra')

# Example 2: checking if a list is in order
ordered = True

# Looping indirectly over the list. The indices of the values in the list
# are assigned to the loop variables.
for n in range(len(pets) - 1):
    if pets[n] > pets[n + 1]:
        ordered = False

if ordered:
    print('The pets list is ordered')
else:
    print('The pets list is not ordered')
    

# List concatenation (just like string concatenation)
xlist = [1, 2, 3]
print(xlist)

xlist = xlist + ['four', 'five', 'six']
print(xlist)

xlist += [7, 8, 9]
print(xlist)

xlist += [10]
print(xlist)


# list repetition (just like string repetition)
xlist = [1, 2, 3]
print(xlist)

xlist = xlist * 3
print(xlist)

xlist *= 2
print(xlist)


# List slicing - obtaining a subset of a list
pets = ['cat', 'dog', 'gerbil', 'hamster', 'rabbit', 'turtle']

print(pets)
print(pets[0:6:1])
print(pets[:])
print(pets[1:4])
print(pets[0:4:2])

# out-of-bounds slices - no error!
print(pets[0:999])
print(pets[-999:6])
#print(pets[999])     # out-of-bounds indexing _does_ cause an error

# Other useful functions: del, min, max
print(pets)
del pets[5]     # remove the item at index 5 from the pets list
print(pets)

# Note: the elements of the pets list much be orderable or these functions
# will crash, e.g., don't use min() on a list with both strings and numbers.
print(min(pets))
print(max(pets))


# Boolean flags
# Search a list for a specific item
pets = ['cat', 'cow', 'dog', 'horse', 'pig', 'zebra']

# Assume zebra is _not_ in the list becauses it is easy to disprove if
# the assumption is incorrect
zebra = False

for animal in pets:
    if animal == 'zebra':     # Note that there is no else clause!
        zebra = True

if zebra:
    print('Yes, we have a zebra.')
else:
    print('No, we don\'t have a zebra')

# Checking that a list is in order
# Assume that the list is in order because it is easy to disprove if the
# assumption is incorrect
ordered = True

for n in range(len(pets) - 1):
    if pets[n] > pets[n + 1]:
        ordered = False

if ordered:
    print('The pets list is ordered')
else:
    print('The pets list is not ordered')


# List methods
# IMPORTANT - most of these directly modify the list and
# return None.
pets = ['cat', 'cow', 'dog', 'horse', 'pig', 'zebra']

print(pets)
pets.append('rat')
print(pets)
# Note that setting new_pets to the result of append() doesn't assign the
# new list to new_pets. new_pets is just equal to None.
new_pets = pets.append('rat')
print(new_pets)

pets.append('dog')
print(pets)

# index()
dog_1 = pets.index('dog')
print(dog_1)
dog_1 = pets.index('dog')
print(dog_1)

# insert()
print(pets)
pets.insert(2, 'snake')
print(pets)

# remove()
pets.remove('dog')
print(pets)
