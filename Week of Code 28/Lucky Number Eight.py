#!/bin/python
import sys
import itertools


n = int(raw_input().strip())
number = raw_input().strip()
# your code goes here
lst = []
s = str(number)
for i in xrange(0,n) :
	lst.append(s[i])
count = 0
for L in range(1, len(lst)+1):
    for subset in itertools.combinations(lst, L):
        q = list(subset)
        q = ''.join(q)
        if(int(q)%8 == 0) :
        	count = count +1
print count