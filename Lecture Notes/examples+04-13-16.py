# Puzzle - read ints from a file and return them in a list
def read_and_make_list(filename):
    my_file = open(filename, 'r')

    num_list = []
    for line in my_file:
        #line = line.rstrip('\n')
        #line = int(line)
        num_list.append(int(line))

    my_file.close()
    return num_list

new_list = read_and_make_list('numbers.txt')

print(new_list)


# Learning to use the zlib compression library
# Let's experiment and try to figure it out...
import zlib

# We need a 'b' in front of the string to convert it to bytes,
# because it turns out that the compress() method only works
# with bytes, not with strings.
#data = b'The quick brown fox jumps over the lazy dog'

# The encode() method converts a string to bytes, just like
# putting 'b' in front of the string converts it to bytes.
data = 'The quick brown fox jumps over the lazy dog'
data = data.encode()

# compress the data
data_compressed = zlib.compress(data)

print(data_compressed)

# uncompress the data
data_uncompressed = zlib.decompress(data_compressed)

# decompress returns a bytes object, but we can convert that to
# a string by using the decode() method.
data_uncompressed = data_uncompressed.decode()
print(data_uncompressed)


# Let's write a function to compress a file
def comp106():
    filename = input('Enter name of file to be compressed: ')

    file = open(filename, 'r')
    data = file.read()
    file.close()

    data = data.encode()
    compressed = zlib.compress(data)

    # Let's append '.comp' to the original file name to create
    # our output file name. Note that the file mode it 'wb' to
    # allow us to write bytes instead of strings.
    comp_file = open(filename + '.comp', 'wb')
    comp_file.write(compressed)
    comp_file.close()

comp106()

# Let's write a function to decompress a file
def decomp106():
    filename = input('Enter name of *.comp file: ')

    # The compressed file contains bytes, not a string, so open
    # in mode 'rb'
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    # decompress the data
    original = zlib.decompress(data)

    # strip '.comp' from end of filename, and add 'new_' to the
    # front. This time we use mode 'w' because we're writing a
    # string.
    original = original.decode()
    new_file = open('new_' + filename.rstrip('.comp'), 'w')
    new_file.write(original)
    new_file.close()

decomp106()


# We compressed data.txt from 803 KB to 9KB - that's 98.9%
# compression! Can we keep compressing it?
#
# Size (KB)   filename                  Compression
# ------------------------------------------------
#    803      data.txt                       -
#      9      data.txt.comp                98.9%
#      4      data.txt.comp.comp           99.5%
#      4      data.txt.comp.comp.comp      99.5%
#
# It turns out that there's only so far we can compress a file.
# Information theory tells us that there's an intrinsic amount
# of information in the file, and that limits how far we can
# compress it.
