# Non Abundant Sum

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the 
# proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant 

# numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two 
# abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest 
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


import math
import functools as ft
import timeit 

@ft.lru_cache(maxsize=None)
def abundant(num):
	sumdivs = 1
	for i in range(2,math.floor(num/2)+1): 
		if num%i == 0:
			sumdivs += i

	if sumdivs > num:
		return True
	return False


total = 0
start=timeit.default_timer() 
for num in range(1,28124):
	flag = True
	for j in range(1,math.floor(num/2)+1):
		if abundant(j) and abundant(num-j):
			flag = False
			break
	if flag:	
		total += num
end = timeit.default_timer()


print(total)
print('total time:')
print(end-start)