# exception handling
# division by 0 error
5 / 0

# value error
int('a')

# file not found error
file = open('non_existent_file.zzz', 'r')

# Using try-except to gracefully handle exceptions
dividend = 25

def my_function():
    # This catches input that can't be converted to a float
    try:
        divisor = float(input('Enter a divisor: '))

    except ValueError:
        print('Sorry - the input must be numeric')
        return

    # This catches divison by 0 errors
    try:
        quotient = dividend / divisor

    except ZeroDivisionError:
        print('Sorry - the input must be non 0')
        return
    
    print(dividend, '/', divisor, '=', quotient)

# The try-except statements can be combined
def my_function():
    try:
        divisor = float(input('Enter a divisor: '))
        quotient = dividend / divisor

    except (ValueError, ZeroDivisionError):
        print('Sorry - the input must be numeric and not 0.')
        return
    
    print(dividend, '/', divisor, '=', quotient)

my_function()


# Using except without specifying an exception catches all
# exception, including KeyboardInterrupt. This is bad practice.
# Only catch those exceptions that you anticipate, because those
# are the only ones you can handle gracefully.

# You can't ctrl-c out of the following code because it catches
# all exceptions, including Keyboardinterrupt.
response = 0
while response != '':
    try:
        response = input('Enter a response: ')

    except:
        print('I\'m sorry Dave. I\'m afraid I can\'t do that.')


# Input testing with exception handling. This would be useful
# for something like Program 1, where the user might input
# something non-numeric for the answer to a math question.
valid_input = False
while not valid_input:
    try:
        value = int(input('Enter an integer: '))
        valid_input = True

    except ValueError:
        print('Error - only integer values are allowed.')
