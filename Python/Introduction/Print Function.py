# Enter your code here. Read input from STDIN. Print output to STDOUT
x = raw_input()
x = int(x)
i = 1
p = 0
while (i<=x) :
    if i< 10 :
        p = p*10 + i
    elif i>=10 and i<100 :
        p = p*100 +i
    elif i>=100 and i<10000 :
        p = p*1000 +i
    i = i+1
print p