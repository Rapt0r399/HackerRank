# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
n = int(n)
d = dict()
for i in range(n) :
    p = raw_input()
    q = raw_input()
    q = float(q)
    d[p] = q
l =sorted(d.values())
a = l[0]
l1 = list()
sl = 0.0
m =0
for i in range(n) :
    if l[i] > a :
        sl = l[i]
        break
for k,v in d.items() :
    if(v == sl) :
        l1.append(k)
        m = m+1
l1.sort()
for i in range(m) :
    print l1[i]