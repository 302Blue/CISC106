from cisc106_34 import *

def linear_search(values, tagrget):
    ''' This function searches for the first occurrence of "target" in
        "values" list. If found, the index of "target" is returned,
        otherwise None is returned.
    Parameters:
        values (list)
        target (any)
    Returns:
        (int) - index where target was found in values
        None - if target not found
    '''
    # loop over values list searching for target
    for n in range(len(values)):
        if values[n] == target:
            return n

    # value not found
    return None

assertEqual(linear_search(['x', 'e', 'w', 'q', 'z', 'r'], 'z'), 4)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 7), 1)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 4), 0)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], -7), None)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 5), None)
