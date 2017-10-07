def printStars(value):
	if (value > 0):
		print('*', end = '')
		value = value - 1
		printStars(value)
printStars(8)
