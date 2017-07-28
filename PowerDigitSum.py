""" Power Digit Sum """

"""

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

import math, functools

def pds(num,power):
  return functools.reduce(lambda a,b: a+b,
                          [int(i) for i in str(pow(num,power))])
  
if __name__ == "__main__":  
	print(pds(2,1000))  