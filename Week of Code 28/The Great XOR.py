#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    # your code goes here
    c = 0
    for i in xrange(1,x) :
        if(i^x>x) :
            c+= 1
    print c
