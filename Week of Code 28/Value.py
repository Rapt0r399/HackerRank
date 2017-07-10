#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    lst = [None]*n
    out = 0
    for a1 in xrange(m):
        x,y = raw_input().strip().split(' ')
        x,y = [int(x),int(y)]
        # your code goes here
        if(lst[x-1] == None and lst[y-1]==None) :
        	lst[x-1] = str(y)
        	lst[y-1] = str(x)
        elif(lst[x-1] == None) and lst[y-1].find(str(x)) == -1 :
        	lst[x-1] = str(y)
        	lst[y-1] = lst[y-1] +(str(x))
        elif(lst[y-1]==None) and lst[x-1].find(str(y)) == -1 :
        	lst[x-1] = lst[x-1] +(str(y))
        	lst[y-1] = str(x)
        elif lst[x-1].find(str(y)) == -1 and lst[y-1].find(str(x)) == -1 :
        	lst[x-1] = lst[x-1] +(str(y))
        	lst[y-1] = lst[y-1] +(str(x))
        for i in xrange(n) :
            q  = lst[i]
            if q != None :
	        	for j in q :
	        		m = lst[int(j)-1]
	        		if m!= None :
		        		for k in m :
		        			if lst[i].find(k) == -1 and int(k)-1 != i :
		        				lst[i] = lst[i] + k
        k = 0
        for i in xrange(n) :
        	if lst[i] != None :
        		k = k + len(lst[i])
        out = out + k
    print out