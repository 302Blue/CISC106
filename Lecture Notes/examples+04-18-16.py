# Using Matplotlib's pyplot module
import matplotlib.pyplot as plt

# plotting with pyplot
plt.plot([1, 2, 3, 4], 'ro')
plt.show()

# plotting x versus y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro--')
plt.show()

# plotting multiple curves
x = [1, 2, 3, 4, 5]
y1 = x
y2 = [1, 4, 9, 16, 25]
y3 = [1, 8, 27, 64, 125]
plt.plot(x, y1, 'go-.', x, y2, 'r^-', x, y3, 'bs--')
plt.show()

# setting the axes
plt.axis([0, 6, 0, 150])
x = [1, 2, 3, 4, 5]
y1 = x
y2 = [1, 4, 9, 16, 25]
y3 = [1, 8, 27, 64, 125]
plt.loglog(x, y1, 'go-.', x, y2, 'r^-', x, y3, 'bs--')
plt.show()

# other plot types
# plt.semilogy()
# plt.loglog()

# adding axis labels and a title
plt.xlabel('list index')
plt.ylabel('list values')
plt.title('Plotting with Matplotlib\'s Pyplot Module')
plt.plot([1, 2, 3, 4], 'ro-')
plt.show()

# pie chart (without labels)
data = [20, 26, 17, 6, 5]
plt.title('Matplotlib Pie Chart')
plt.pie(data)
plt.show()

# list of of favorite fruits for 100 people
favorites = ['oranges', 'nectarines', 'oranges', 'nectarines', 'cherries',
             'nectarines', 'oranges', 'oranges', 'oranges', 'grapes',
             'nectarines', 'oranges', 'apples', 'oranges', 'oranges',
             'oranges', 'apples', 'apples', 'grapes', 'oranges',
             'oranges', 'bananas', 'oranges', 'apples', 'cherries',
             'apples', 'oranges', 'nectarines', 'apples', 'bananas',
             'grapes', 'oranges', 'cherries', 'oranges', 'oranges',
             'bananas', 'nectarines', 'bananas', 'nectarines', 'nectarines',
             'bananas', 'oranges', 'bananas', 'bananas', 'bananas',
             'nectarines', 'oranges', 'oranges', 'grapes', 'bananas',
             'nectarines', 'apples', 'cherries', 'oranges', 'grapes',
             'oranges', 'oranges', 'grapes', 'nectarines', 'grapes',
             'apples', 'bananas', 'nectarines', 'cherries', 'cherries',
             'grapes', 'oranges', 'oranges', 'oranges', 'bananas',
             'apples', 'oranges', 'bananas', 'oranges', 'nectarines',
             'bananas', 'apples', 'oranges', 'cherries', 'bananas',
             'apples', 'nectarines', 'nectarines', 'apples', 'nectarines',
             'nectarines', 'nectarines', 'apples', 'cherries', 'apples',
             'nectarines', 'oranges', 'apples', 'nectarines', 'nectarines',
             'oranges', 'apples', 'bananas', 'cherries', 'apples']

fruits = ['apples', 'bananas', 'oranges', 'cherries', 'nectarines', 'grapes']
# To display this data in a pie chart, you need to determine how many values
# there are in each category - the pie() function will not do that for you.
# Below is a list containing the counts for each category.
fruit_counts = [17, 15, 30, 9, 21, 8]
plt.pie(fruit_counts)
plt.show()


# When working with numberic data, the histogram function (unlike the pie()
# function,), doesn't need to be told how many items are in each bin
# (category). It only needs to be given the values, and it will figure out
# how many are in each bin.
# Creating a histogram
data = [20, 26, 17, 6, 5]
plt.hist(data)
plt.show()

# histogam with bins and axes specified
data = [20, 26, 17, 6, 5, 30]
bins = [0, 5, 10, 15, 20, 25, 30]
plt.axis([0, 30, 0, 4])
plt.hist(data, bins)
plt.show()

# histogram with non-uniform bins
data = [20, 26, 17, 6, 5, 30]
bins = [0, 15, 20, 25, 30]
plt.hist(data, bins)
plt.show()

# histogram of a random normal distribution
import random as rnd
n_points = 1000
x_list = []
y_list = []
for n in range(n_points):
    x_list.append(rnd.normalvariate(0.0, 1.0))
    y_list.append(rnd.normalvariate(0.0, 1.0))

plt.hist(x_list, 25)
plt.show()

# other plot types
# scatter()
# stacked()
# bar()
# barh()

# scatter plot of data from a random normal distribution
plt.scatter(x_list, y_list)
plt.show()

# multiple line plots with legend
x = [1, 2, 3, 4, 5]
y1 = x
y2 = [1, 4, 9, 16, 25]
y3 = [1, 8, 27, 64, 125]
plt.axis([0, 6, 0, 150])
plt.xlabel('x-values')
plt.ylabel('x, x^2, x^3')
plt.title('Powers of x')
plt.plot(x, y1, 'go-.', x, y2, 'r^-', x, y3, 'bs--')
# loc can be "upper left", "lower right", "center", "center right", etc.,
# and it can also be 'best'.
# Call the legend function _AFTER_ calling the plot function.
plt.legend(['x', 'x^2', 'x^3'], loc = 'best')
plt.show()


# Recursion
# non-recursive countdown function
def countdown_nr(n):
    for count in range(n, 0, -1):
        print(count)

    print('Blastoff!')

countdown_nr(10)

# recursive countdown function
def countdown(n):
    # check for base case
    if n == 0:
        print('Blastoff!')
        return

    # handle recursive case
    print(n)
    countdown(n - 1)
    return

countdown(10)

# recursive n! function
def factorial(n):
    # check for the base case
    if n == 0:
        return 1

    # handle the recursive case
    return n * factorial(n - 1)

k = 100
print(k, '! = ', factorial(k), sep = '')
