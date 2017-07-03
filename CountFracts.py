# REDUCED PROPER FRACTION 

# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction. 
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get: 
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8 
# It can be seen that there are 21 elements in this set. 
# How many elements would be contained in the set of reduced proper fractions for d ≤ 10,000? 
 

import timeit 
  
#finding HCF using Euclidean Algorithm: 
  
def getHCF(x,y): 
	while(y): 
		x,y = y,x%y 
	return x 


def RPF(d): 
	return sum([1 for x in range(1,d) for y in range(2,d+1) if getHCF(x,y) == 1 and x<y]) 


start=timeit.default_timer() 
print(RPF(1000000)) 
end=timeit.default_timer() 
print(end-start) 
