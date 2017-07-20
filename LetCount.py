# Number letter count

# If the numbers 1 to 5 are written out in words: one, 
# two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
# letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were 
# written out in words, how many letters would be used? 
# NOTE: Do not count spaces or hyphens. For example, 342 
# (three hundred and forty-two) contains 23 letters and 115 
# (one hundred and fifteen) contains 20 letters. The use of "and" 
# when writing out numbers is in compliance with British usage.


import math


def lettercount(num):
	# Pick the unique ones to store in the dictionary
	numdict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3,
	            7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6,
	           13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8,
	           19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5,
	           70: 7, 80: 6, 90: 6}
	letterlen = 0
	if (num == 1000):
		letterlen = 11
	else:
		try:
			numdict[num]
			letterlen += numdict[num]
		except:
			rem = num % 100
			if(rem == num):
				letterlen += numdict[math.floor(num/10) * 10]
				if (num % 10 != 0):
					letterlen += numdict[num % 10]
			else:
				letterlen += numdict[math.floor(num/100)] + 7
				if (rem != 0):
					num = num - (math.floor(num/100)*100)
					letterlen += lettercount(num) + 3
	return letterlen


length = 0
for each in range(1, 1001):
	length += lettercount(each)
print(length)
