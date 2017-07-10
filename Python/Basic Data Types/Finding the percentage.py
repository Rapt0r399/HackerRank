# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
n = int(n)
d = dict()
for i in range(n) :
    p =raw_input()
    q = p.split()
    score  = map(float, q[1:])
    d[q[0]] = sum(score) / float(len(score))
name = raw_input()
for k,v in d.items() :
    if(k == name) :
        print "%.2f" % v