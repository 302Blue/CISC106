# Searching
# linear search
from cisc106_34 import assertEqual

def linear_search(int_list, target):
    # serach list for target value
    for i in range(len(int_list)):
        if int_list[i] == target:
            return i

    # target not found, return None
    return None

# binary search
def binary_search(int_list, target):
    # initialize low, mid, and high
    low = 0
    high = len(int_list) - 1
    mid = (low + high) // 2

    # loop until low and high cross, or until target is found
    while low <= high:
        if int_list[mid] == target:
            return mid                  # return index if target is found
        elif target < int_list[mid]:    # target below mid
            high = mid - 1              # move high
            mid = (low + high) // 2     # recalculate mid
        else:                           # target above mid
            low = mid + 1               # move low
            mid = (low + high) // 2     # recalculate mid

    # target not found
    return None

# Timing searches
# For Mac, linux, and unix, use time.time()
# For Windows, use time.clock()
# Both functions provide microsecond accuracy. The only difference is that
# time() returns the current time, and clock() returns the elapsed time
# since this first call to clock().
import time
import random as rnd

# create a list of size N
N = 100000000
start = time.time()
big_list = list(range(N))
print('Time to build big list =', time.time() - start)

# pick the target value at random
k = rnd.randint(0, N - 1)

# Time the linear search
start = time.time()
lin_ind = linear_search(big_list, k)
lin_time = time.time() - start

print()
print('Total linear search time =', lin_time, 'seconds')
print('linear =', format(lin_ind, ',d'))

# Time the binary search
start = time.time()
bin_ind = binary_search(big_list, k)
bin_time = time.time() - start

print()
print('Total binary search time =', bin_time, 'seconds')
print('binary =', format(bin_ind, ',d'))

# How much faster is binary search?
print()
print('Binary search was',
      format(int(lin_time/bin_time), ',d'), 'time faster')
