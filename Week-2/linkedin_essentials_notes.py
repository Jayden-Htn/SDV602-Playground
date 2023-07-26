# I am picking out select videos from the Linkedin course: Python Essential Training (2022) by Ryan Mitchell.
# I have a strong background in Python, so I am only watching any videos that I think I might learn something new from.


# <---- Bytes ---->
b = bytes(4)
b = b'\x00\x00\x00\x00' # b'string' is a byte string
# stores values in hexidecimals (base 16), prepresenting each byte as two hex digits


# <---- Int Base ---->
# int() can take a base argument, must be string
# base 2 is binary, base 8 is octal, base 16 is hexadecimal
print(int('101', 2)) # 5


# <---- Bool Casting ---->
# bool() can take any object and return True or False
bool(-1) # any number except 0 is true