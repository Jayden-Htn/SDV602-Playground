# Following the Linkedin course: Python Essential Training (2022) by Ryan Mitchell.
# I have a strong background in Python, so this is most a quick refresher for me, but also to gain any small extra pieces of knowledge.


# <---- 4: Basic Data Structures ---->

# 4.1

# list slicing
mylist = [1, 2, 3, 4, 5]
mylist[0] # = 1
mylist[0:3] # = [1, 2, 3]
mylist[0:6:2] # = [1, 3, 5]
mylist[::2] # = [1, 3, 5] # can have empty start and stop values
mylist[::-1] # = [5, 4, 3, 2, 1] # steps backwards
# format: list[start:stop:step]

# creating lists with ranges
newlist = list(range(0, 10)) # = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list methods
mylist.append(6) # = [1, 2, 3, 4, 5, 6], adds to end of list
mylist.insert(0, 0) # = [0, 1, 2, 3, 4, 5, 6], inserts at specified index
mylist.extend([7, 8, 9]) # = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], adds a list to the end of a list
mylist.remove(9) # = [0, 1, 2, 3, 4, 5, 6, 7, 8], specify value to remove
mylist.pop() # = [0, 1, 2, 3, 4, 5, 6, 7], removes last element and returns

# variable references
a = [1, 2, 3]
b = a # b is a reference to a
b[0] = 0 # = [0, 2, 3]
a # = [0, 2, 3]
# both reference the same list, so changing one changes the other
c = [1, 2, 3]
d = c.copy() # d is a copy of c
d[0] = 0 # = [0, 2, 3]
c # = [1, 2, 3]

# 4.2

# sets
myset = {1, 2, 3, 4, 5} # can only contain unique values
# can't use indexing or slicing as it is unordered
myset.pop() # removes and returns a random element
myset.remove(5) # removes 5 from the set
myset.add(5) # adds 5 to the set
myset.update([5, 6, 7]) # adds a list to the set
myset.discard(5) # removes 5 from the set, but doesn't throw an error if it doesn't exist

# tuples
mytuple = (1, 2, 3, 4, 5) # immutable, can't be changed
# much more space efficient than lists
# functions that return multiple values, return tuples by default

# declare multiple values
a, b, c = 1, 2, 3
# or could do a, b, c = return_multiple_values(), packs the tuple into the variables

# 4.3

# dictionaries
mydict = {'name': 'John', 'age': 23, 'height': 1.8} # key-value pairs
mydict['name'] # retrieve value
mydict.get('last_name', 'Doe') # retrieve value, if key doesn't exist, return default value. No default -> returns None
mydict['age'] = 24 # update value
mydict['weight'] = 80 # add new key-value pair
# convention to leave atrailing comma after the last value because it makes it easier to add more values later
mydict.keys() # returns a list of keys
mydict.values() # returns a list of values

# default dictionaries
from collections import defaultdict
ddict = defaultdict(list) # creates a dictionary with default values of empty lists
ddict('a').append(1) # = {'a': [1]}
# automatically creates a list if the key doesn't exist
# can also use int, float, etc. as the default value



