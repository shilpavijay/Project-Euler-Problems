# 1000-digit Fibonacci number

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.a

# Hence the first 12 terms will be:

# F1 = 1
#  F2 = 1
#  F3 = 2
#  F4 = 3
#  F5 = 5
#  F6 = 8
#  F7 = 13
#  F8 = 21
#  F9 = 34
#  F10 = 55
#  F11 = 89
#  F12 = 144

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import functools

@functools.lru_cache(maxsize = None)
def Getfib(num):
	if num > 1:
		return Getfib(num-1) + Getfib(num-2)
	return num

i = 15
while(len(str(Getfib(i))) < 1000):
	i += 1
print(i)

print(Getfib.cache_info())
