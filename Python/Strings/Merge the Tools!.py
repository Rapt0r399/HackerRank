# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
k = raw_input()
k = int(k)
n = len(s)
r = n/k
l = list()
l2 = list()
for i in xrange(0,n,k) :
    l.append(s[i:i+k])
for i in range(r) :
    l1 = list()
    flag =0
    for j in range(len(l[i])) :
        if (l[i].count((l[i])[j])==1) :
            l1.append((l[i])[j])
        elif (l[i].count((l[i])[j])>=1 and flag == 0) :
            if not (l[i])[j] in l1 :
                l1.append((l[i])[j])
    l2.append(''.join(l1))
for i in range(r) :
    print l2[i]