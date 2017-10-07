# File I/O - opening/closing/reading/writing files. (r, w, a)
# write mode - if file doesn't exist, creates new file
#              if file exists, deletes contents of existing file!
my_file = open('test.txt', 'w')
my_file.write('This is a simple test of Python file access\n')
my_file.close()

# read mode - file must already exist
my_file = open('test.txt', 'r')
contents = my_file.read()     # read() method reads entire contents of file
my_file.close()
print(contents)

# append mode - write additional information to the end of a file
#             - if file doesn't exist, first create it
my_file = open('test.txt', 'a')
my_file.write('Adding another line to the file...\n')
my_file.close()

# read file to confirm contents
my_file = open('test.txt', 'r')
contents = my_file.read()
my_file.close()
print(contents)

# write mode with existing file - content is erased!
my_file = open('test.txt', 'w')
my_file.close()

# using readline() to read a file one line at a time
my_file = open('test.txt', 'r')
line = my_file.readline()
print(line)
line = my_file.readline()
print(line)
line = my_file.readline()
print(line)
line = my_file.readline()
print(line)
my_file.close()

# stripping newline characters - every line ends with a newline character
my_file = open('test.txt', 'r')
line = my_file.readline()
line = line.rstrip('\n')
print(line)
line = my_file.readline()
line = line.rstrip('\n')
print(line)
line = my_file.readline()
line = line.rstrip('\n')
print(line)
my_file.close()


# reading a file line-by-line and detecting EOF (End Of File)
# using a while loop
my_file = open('test.txt', 'r')

line = my_file.readline()   # priming the loop

while line != '':           # read until readline() return the empty string
    line = line.rstrip('\n')
    print(line)
    line = my_file.readline()

my_file.close()

# using a for loop (This method if preferred)
# Just as Python sees a list as a sequence of values that you can loop over,
# and just as Python sees a string as a sequence of characters that you can
# loop over, so too does Python see a file as a sequence of lines that you
# can loop over.
my_file = open('test.txt', 'r')

for line in my_file:     # loop automatically stops when EOF is reached
    line = line.rstrip('\n')
    print(line)

my_file.close()


# Pathnames (Mac/PC)
# relative paths
# Mac versions
my_file = open('test.txt', 'r')
my_file = open('examples/test.txt', 'r')
my_file = open('../test.txt', 'r')
my_file = open('../examples/test.txt', 'r')

# Windows versions
my_file = open(r'examples\test.txt', 'r')
my_file = open(r'..\test.txt', 'r')
my_file = open(r'..\examples\test.txt', 'r')

# absolute path
my_file = open('/Users/jon/Desktop/test.txt', 'w')
my_file = open(r'C:\Users\jon\Desktop\test.txt', 'w')

# write code to print contents of a file specified by user
filename = input('Enter name of file: ')

file = open(filename, 'r')
contents = file.read()
file.close()

print(contents)


# Puzzle - read ints from a file and return them in a list
def read_and_make_list(filename):
    my_file = open(filename, 'r')

    num_list = []
    for line in my_file:
        line = line.rstrip('\n')
        line = int(line)
        num_list.append(line)

    my_file.close()
    return num_list

new_list = read_and_make_list('numbers.txt')

print(new_list)
