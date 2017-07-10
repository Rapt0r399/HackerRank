# Enter your code here. Read input from STDIN. Print output to STDOUT
import hashlib
n = raw_input()
n = int(n)
a = raw_input()
b = a.split()
for i in xrange(n):
    b[i] = int(b[i])
t = tuple(b)
print hash(t)