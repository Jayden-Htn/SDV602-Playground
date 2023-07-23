# Following along with the linkedin course: Python for Non-Programmers by Nick Walter.
# I have a strong background in Python, so this is a quick refresher for me.


# <---- 2: Project 1 Fortune Cookie ---->

# 2.1
import random

num = random.randint(1, 3)

if num == 1:
    print("You will have a great day today!")
elif num == 2:
    print("Things will go your way today.")
else:
    print("Enjoy a wonderful day of success.")


#  2.2
lucky_number = random.randint(1, 100)
fortune_number = random.randint(1, 3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = "You will have a great day today!"
elif fortune_number == 2:
    fortune_text = "Things will be okay."
else:
    fortune_text = "Today might be tough."

print(f"{fortune_text} Your lucky number is {lucky_number}.")
