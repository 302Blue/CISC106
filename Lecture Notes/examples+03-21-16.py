# How to test if a value is even or odd
number = int(input('Enter an integer: '))

if number % 2 == 0:
    print(number, 'is even')
else:
    print(number, 'is odd')

# How to test if a number is a multiple of 7
if number % 7 == 0:
    print(number, 'is a multiple of 7')
else:
    print(number, 'is not a multiple of 7')


# What does this function return?
def check_size(size):
    if size > 10:
        return 'XL'
    elif size > 8:
        return 'L'
    elif size > 6:
        return 'M'
    elif size > 4:
        return 'S'
    else:
        return 'XS'

    return None

# Following function call causes the function to return 'M'. The function
# does _NOT_ return None. Once you reach a return statement in a function,
# you leave the function without executing any other statements in the
# function. In particular, you don't reach the return None statement at
# the end of the function. In fact, it is not possible to reach that
# statment.
result = check_size(7)
print(result)
