
def fizzbuzz(f_num, b_num, up_to):
    i = 1
    list = []
    while i <= up_to:
        if i % f_num == 0 and i % b_num == 0:
            list.append((i, 'FizzBuzz'))
        elif i % f_num == 0:
            list.append((i, 'Fizz'))
        elif i % b_num == 0:
            list.append((i, 'Buzz'))
        else:
            list.append((i, str(i)))
        i += 1
    return list

fizzbuzz_list = fizzbuzz(3, 5, 20)
print(fizzbuzz_list)
    