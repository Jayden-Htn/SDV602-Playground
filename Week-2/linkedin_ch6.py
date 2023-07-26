# Following along with the linkedin course: Python for Non-Programmers by Nick Walter.
# I have a strong background in Python, so this is a quick refresher for me.


# <---- 6: Project 3 Number Guesser ---->

# 6.1 and 6.2
import random
import time


print("Welcome to the Number Guesser!")
print("I'm thinking of a number between 1 and 10...")
time.sleep(3)
print("Done! Now try to guess what it is.")
guess = int(input("Guess a number between 1 and 10: "))
correct_number = random.randint(1, 10)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess > correct_number:
        print("\nToo high!")
    else:
        print("\nToo low!")
    guess = int(input("Guess again: "))
    
print("You win! It took you", guess_count, "guesses.")
