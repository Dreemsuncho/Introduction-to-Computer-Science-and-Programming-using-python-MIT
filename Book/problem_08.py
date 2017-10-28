fib_2_count = 0


def fib(n):
    global fib_2_count
    if n == 2:
        fib_2_count += 1

    if n in [0, 1]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def testFib(n):
    for i in range(n + 1):
        print('fib of ', i, '=', fib(i))


x = int(input('Enter number '))

testFib(x)
print(fib_2_count)
