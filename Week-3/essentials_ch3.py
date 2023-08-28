# Following the Linkedin course: Python Essential Training (2022) by Ryan Mitchell.
# I have a strong background in Python, so this is most a quick refresher for me, but also to gain any small extra pieces of knowledge.


# <---- 3: Basic Data Types ---->

# 3.1

x = int(4.5*1.3) # converting data types is called casting
# int(8.9) -> 8, always round down when going from a float to int (only keeps before the dot)
print(round(8.9, 0))
print(1.2-1.0) # = 0.19999999999999996
# Python's uses data approximation which can impact very small calculations

# 3.2

int('100') # can convert strings to integers
int('100', 2) # can convert strings to integers in different bases (binary, octal, hexadecimal, etc.)

from decimal import Decimal, getcontext # can use the decimal module to get more accurate calculations
getcontext().prec = 2 # sets the precision to 2 decimal places
Decimal(1) / Decimal(7) # = 0.14 because precision is set to 2 decimal places

# 3.3

bool(1) # = True
bool(0) # = False
# any non-0 value is True
bool('False') # = True because it is a non-empty string
bool('') # = False because it is an empty string
# empty lists, tuples, dictionaries, etc. are also False
mylist = [1, 2, 3]
if mylist: # if mylist is not empty, same as writing if bool(mylist):
    print('I found something!')

# 3.4

name = 'My name is John'
name[0] # = 'M', slicing strings
name[0:7] # = 'My', characters 0 to 6
name[11:] # = 'John', characters 11 to the end
name[-4:] # = 'John', last 4 characters
# works the same for list elements
name[0:7:2] # = 'M a', characters 0 to 6, every second character

f'My name is {name[-4:]} and I am {23} years old' # string interpolation with a format string (f string)

import math
f'Pi is approximately {math.pi:.3f}' # :.3f means 3 decimal places
'Pi is approximately {}'.format(math.pi) # old way of string interpolation,string format function

myString = '''
This is a multi-line string
I just keeps going
and going
'''

# 3.5

# bytes are used for storing binary data. They are immutable sequences of bytes. Useful for storing images, videos, etc.
# bytes are immutable, bytearray are mutable
bytes(4) # creates a bytes object of length 4
# output: b'\x00\x00\x00\x00', \x00 is a null byte, uses base 16 numbers which is 8 bits (2^8 = 256)
mybyte = bytes('Hello', 'utf-8') # creates a bytes object from a string
mybyte.decode('utf-8') # converts a bytes object to a string
# useful for sending data over a network, or storing data in a database

b2 = bytearray('Hello', 'utf-8') # creates a bytearray object from a string
b2[0] = 97 # can change the bytes in a bytearray object


