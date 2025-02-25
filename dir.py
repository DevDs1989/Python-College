import time
import timeit


def func1(n):
    return [i for i in range(n)]


def func2(n):
    return list(range(n))


time1 = timeit.timeit(lambda: func1(1000000), number=100)
time2 = timeit.timeit(lambda: func2(1000000), number=100)

print(time1)
print(time2)
