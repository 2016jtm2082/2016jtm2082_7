#!/usr/bin/python

#Program to count number of times a word occurs in the string


#Enter the string

user_input = raw_input(" enter the srting : ")

#Printing the frequency in entered string

word_freq = {}
from collections import Counter
print ("Words and its frequency are-")
lis = sorted(Counter(user_input.split()).items(),key=lambda (a,b):(-b,a))
for word,freq in lis:
    print ("%-10s %d" % (word, freq))
print ('\n')


#printing the top three words
print ("top 3 frequent words:")
lis = sorted(Counter(user_input.split()).items(),key=lambda (a,b):(-b,a))[:3]
for word,freq in lis:
    print ("%-10s %d" % (word, freq))

#permution of each word in string

def perms(s):        
	    if(len(s)==1): 
		return [s]
	    result=[]
	    for i,v in enumerate(s):
		result += [v+p for p in perms(s[:i]+s[i+1:])]
	    return result


	print('\n'.join(perms(word))

