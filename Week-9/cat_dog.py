"""
Experimenting with classes and objects.

Demonstrates multiple inheritance, constructor invocation, and method overriding.
Animal -> Cat & Dog -> Cat_Dog
"""

# parent class
class Animal(object):
    def __init__(self, x, y) -> None: # -> None specifies that the function returns nothing
        self.x = x
        self.y = y

    def move(self):
        self.x += 1.0
        self.y += 1.0

    def where(self):
        print(self.x, self.y)

# child class
class Cat(Animal):
    def __init__(self, x, y) -> None:
        # invoke the parent class constructor
        Animal.__init__(self, x, y)

    def move(self):
        self.x -= 1.0
        self.y += 10.0
        print("Cat moved")

# child class
class Dog(Animal):
    def __init__(self, x, y) -> None:
        Animal.__init__(self, x, y)

    def move(self):
        self.x += 10.0
        self.y += 10.0
        print("Dog moved")

# next child class
class Cat_Dog(Cat, Dog):
    def __init__(self, x, y) -> None:
        Cat.__init__(self, x, y)
        Dog.__init__(self, x, y)

    def cat_move(self):
        Cat.move()

dom = Dog(1.0, 1.0)
carrie = Cat(1.0, 2.0)

dom.move()
carrie.move()

dom.where()
carrie.where()

cd = Cat_Dog(1.0, 1.0)
cd.move()
cd.where()