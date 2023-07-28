
def fizzbuzz(up_to):
    i = 1
    list = []
    while i <= up_to:
        if i % 3 == 0 and i % 5 == 0:
            list.append((i, 'FizzBuzz'))
        elif i % 3 == 0:
            list.append((i, 'Fizz'))
        elif i % 5 == 0:
            list.append((i, 'Buzz'))
        else:
            list.append((i, str(i)))
        i += 1
    return list

fizzbuzz_list = fizzbuzz(20)
print(fizzbuzz_list)
    