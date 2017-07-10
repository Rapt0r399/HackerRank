# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
p = raw_input()
l = list(s)
q = p.split()
l[int(q[0])] = q[1]
s = "".join(l)
print s