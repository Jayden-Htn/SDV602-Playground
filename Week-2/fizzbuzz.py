
def fizzbuzz(up_to):
    for i in range(1, up_to + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i += 1

fizzbuzz(20)
    