# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors 
# of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.


# Solution:

# Evaluate the sum of all the amicable numbers under 10000.

import math
import functools as ft


def properdiv(num):
	propdiv = [1]
	# until half the number
	divs =  [i for i in range(2, (math.floor(num / 2) + 1)) if num % i == 0]  
	propdiv.extend(divs)
	return propdiv


#returns true if amicable
def checkamicable(n1, n2):			
	def add(a,b): return a+b
	div1 = ft.reduce(add, properdiv(n1))
	div2 = ft.reduce(add, properdiv(n2))
	# not amicable with itself
	if (div1 == n2) and (div2 == n1) and (div1 != n1) and (div2 != n2):  
		return True
	else:
		return False


amiclist = []
for i in range(1, 10000):
	total = ft.reduce(lambda a, b: a+b, properdiv(i))
	if total < 10000 and checkamicable(total, i):
	  amiclist.append(i)

print(amiclist)
print(ft.reduce(lambda a, b: a+b, amiclist))
