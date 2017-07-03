# Name Scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by 
# sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical 
# position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in 
# the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?



# Solution:


#function to get the alphabetical value
def alphval(name):
	name = name.strip('"')

	#create a map for each alphabet with its value
	valmap = {chr(each):each-64 for each in range(65,91)}

	val = 0
	for l in name:
		val += valmap[l]
	return val



#open the file
fl = open('names.txt','r')
namelist = ''

#loop through the file handler to obtain a string of all names
for each in fl:
	namelist += each

#obtain a list  
lst = namelist.split(',')

#sort the list in alphabetical order
lst.sort()

#get the total score:
score = 0
for item in lst:
	score += alphval(item) * (lst.index(item) + 1)

#testing
# print((lst.index('"COLIN"')+1) * alphval("COLIN"))

print(score)