# Following along with the linkedin course: Python for Non-Programmers by Nick Walter.
# I have a strong background in Python, so this is a quick refresher for me.


# <---- 5: Functions and More ---->

# 5.1
def bark():
    print("Woof!")

for i in range(3):
    bark()


# 5.2
def hello(name):
    print(f"Hello {name}!")

hello("John")


def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(5, 7)


# 5.3
def double(num):
    return num * 2

new_num = double(5)
print(new_num)


def capitalise(word):
    return word.upper()

print(capitalise("hello"))


# 5.4
wallet = 20
wallet -= 8 # bought food
wallet += 10 # found money


# 5.5
text = input("Enter some text: ")
print(text)

num = int(input("Enter a number: "))
print(num + 5)