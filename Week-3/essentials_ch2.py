# Following the Linkedin course: Python Essential Training (2022) by Ryan Mitchell.
# I have a strong background in Python, so this is most a quick refresher for me, but also to gain any small extra pieces of knowledge.


# <---- 2: Quick Start ---->

# 2.1

x = 1
name = 'Sam'
print(type(name))
y = 1.7
yes = True
print(type(2j)) # j = imaginary number
print(1j*1j)
print('1' + '1') # = 11
print(1 == 1)


# 2.2

list = [1, 'two', True, 1.5, [1,2,3]]
print(len(list))

set = {1,2,3} # all items must be unique
len({1,1,2,2}) # 2
print({1,1,2,2})
print({1,2} == {2,1}) # True, order doesn't matter in sets

tuple = (1,2,3)
print(len(tuple))
# tuple.append(4) # throws error, once declared it is immutable
# tuples are more memory eficient as Python doesn't need to preallocate extra space for expansion

dict = {'apple': 'Yummy', 'amount': 3} # key-value pairs, require unique keys


# 2.3

a = 1+1
b = 4*5
c = 2**2 # to the power of, exponentiation
d = 10/5
e = 4%3 # remainder, modulus
f = 'string' + ' 1'
g = 'repeat ' * 4
h = (True == False)
i = (4<5)
j = (2>=2)
k = (True and True)
l = (True or False)
m = (not True)


# 2.4 

a = 5
if (a > 4):
    print('Larger')
elif (a < 4):
    print('Smaller')
else:
    print('Same number')

for i in [1,2,3,4]:
    print(i)


# 2.5

def multiply(a, b):
    return a*b

print(multiply(2,3))

c = [1,2,3]
def addToList(c):
    c.append(4) # don't need to return

addToList(c)
print(c)


# 2.6

class Dog:
    def __init__(self, name):
        # called on initialisation
        # self is the specific instance of the class after bein initialised
        self.name = name
        # instance name = arg name
        self.legs = 4
    
    # add class method
    def speak(self):
        # pass self to access any of the attributes or functions in the class
        print(self.name, 'says bark')

my_dog = Dog('Rover')
second_dog = Dog('Doug')
my_dog.speak() # essentially calls speak() with my_dog passed as the first argument
second_dog.speak()
