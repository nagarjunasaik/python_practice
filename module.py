# import math
# #print(dir(math))

# print(math.factorial(5))
# print(math.sqrt(9))


#Instead of mentioning every time module name, we can use from keyword
#---------------------------------------------------------------------

# from math import factorial,pi,sqrt

# from math import * # imports all the functions in math

# print(factorial(3))

# print (sqrt(25))



#Random: Provides a random number generation and randomness in  a sequence within builtin functionality

# from random import *

#for i in range (0,100):
# 	print(randint(0,100))
i=0
while i<10:
	x=randint(0,5)
	if x == 5:
		print('hello')
		continue
	print(x)
	i+=1

'''Time: 	Give time functionality from all time zomes,  including cpu frequncy 
    and system details this python is using
	
	time() gives sec passed from epoc time from linux publically released

	'''

# from time import *

# #print(time())	


# print(asctime()) # ansyncronous time
# #sleep(<int>) # stop programming for given time in secs
# print(time())
# sleep(7)
# print(time())
# print(sleep())

'''
Calendar:
	Gives calendar functionality

'''
from calendar import *
print(calendar(2018))

print(month(2018,7))

print(week())