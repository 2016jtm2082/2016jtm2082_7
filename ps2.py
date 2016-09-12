#!/usr/bin/python

#program to calculate percentage of user in unit circle

import random
a=0            #variable for number of users


count=0        #variable for number of users in the unit circle
for u in range(1,101):
	(X,Y)=(random.random()*2- 1, random.random()*2-1)
	a+=1
	
	if((X**2+Y**2)<=1):
		count+=1

percentage=(float(count)/100)*100


#Total percentage of user in unit circle around the msc

print "Percentage of users in the unit circle around the MSC is %d" %percentage

