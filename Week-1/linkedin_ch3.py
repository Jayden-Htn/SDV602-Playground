# Following along with the linkedin course: Python for Non-Programmers by Nick Walter.
# I have a strong background in Python, so this is a quick refresher for me.


# <---- 3: Lists, Loops, and Dictionaries ---->

# 3.1
fav_foods = ["Pizza", "Pasta", "Salad", "Bread"]
print(fav_foods)
print(fav_foods[0])

fav_numbers = [1, 2, 3, 4, 5]
print(fav_numbers)
print(len(fav_numbers))


# 3.2
fav_numbers.append(6)
print(fav_numbers)
fav_numbers.insert(0, 0)
print(fav_numbers)
del(fav_numbers[3])
print(fav_numbers)


# 3.3
for num in range(10):
    print(num)

for food in fav_foods:
    print(food)
    
for num in range(40):
    print((num+1)*2)


# 3.4
cats = {"Jane": 5, "Tom": 4, "Sam": 6}
print(cats)
print(cats["Jane"])
cats["Wilson"] = 7
print(cats)
print(len(cats))
