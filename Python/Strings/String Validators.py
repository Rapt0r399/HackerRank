# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
f1=False
f2=False
f3=False
f4=False
f5=False
for i in range(0,len(s)) :
    if(s[i].isalpha()) : f2 = True
    if(s[i].isdigit()) : f3 = True
    if(s[i].islower()) : f4 = True
    if(s[i].isupper()) : f5 = True
if(f2 == True or f3 == True) : print "True"
else : print "False"
if(f2 == True) : print f2
else : print "False"
if(f3 == True) : print f3
else : print "False"
if(f4 == True) : print f4
else : print "False"
if(f5 == True) : print f5
else : print "False"