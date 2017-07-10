# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
n = int(s)
l = len(bin(n)[2:])
for i in range(1,n+1) :
    print str(i).rjust(l,' '), oct(i)[1:].rjust(l,' '), hex(i)[2:].rjust(l, ' ').upper(), bin(i)[2:].rjust(l,' ') 