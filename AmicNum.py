# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors
# of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# Solution:

import math
import functools as ft
import timeit


def properdiv(num):
    propdiv =[1] + [filt for filt in (i for i in range(2, (math.floor(num / 2) + 1)) if num % i == 0)]
    # Loop runs until half the given number
    return propdiv


# Function returns true if the given numbers are Amicable
def checkamicable(n1, n2):
    def add(a, b): return a + b
    div1 = ft.reduce(add, properdiv(n1))
    div2 = ft.reduce(add, properdiv(n2))
    # Check if given number is not amicable with itself
    return True if (div1 == n2) and (div2 == n1) and (div1 != n1) and (div2 != n2) else False


def amicListGen():
    for i in range(1, 10000):
        total = ft.reduce(lambda a, b: a + b, properdiv(i))
        if total < 10000 and checkamicable(total, i):
            yield i


if __name__ == "__main__":
    start = timeit.default_timer()
    amiclist = [i for i in amicListGen()]
    print(ft.reduce(lambda a, b: a+b, amiclist))
    end = timeit.default_timer()
    print('timetaken:' + str(end - start))
