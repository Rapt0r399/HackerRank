# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
n = int(n)
l = list()
t = raw_input()
l = t.split()
for i in range(n) :
    l[i] = int(l[i])
l.sort()
m = l[n-1]
i = n-1
while (i>=0) :
    if(l[i]<m) :
        print l[i]
        break
    i = i-1