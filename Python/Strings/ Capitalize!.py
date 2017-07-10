s = raw_input()
k = s
l = s.split()
n = len(l)
for i in range (n) :
    l[i] =  ''.join((l[i])[0].upper() + (l[i])[1:] )
s = ' '.join(l)
if (len(k) == len(s)) :
    print s
else :
    print k.title()