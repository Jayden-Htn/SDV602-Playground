
def fizzbuzz(up_to):
    i = 1
    list = []
    while i <= up_to:
        if i % 3 == 0 and i % 5 == 0:
            list.append('FizzBuzz')
        elif i % 3 == 0:
            list.append('Fizz')
        elif i % 5 == 0:
            list.append('Buzz')
        else:
            list.append(i)
        i += 1
    return list

fizzbuzz_list = fizzbuzz(20)
print(fizzbuzz_list)
    