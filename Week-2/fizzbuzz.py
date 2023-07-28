
def fizzbuzz(up_to):
    i = 1
    while i <= up_to:
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
    