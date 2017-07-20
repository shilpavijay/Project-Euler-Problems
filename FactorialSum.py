#Factorial Sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import functools


def fact(num):
	prod = 1
	for i in range(1, num + 1):
		prod = prod * i
	return functools.reduce(lambda a, b: a + b, [int(each) for each in str(prod)])


print(fact(100))
