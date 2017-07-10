# Enter your code here. Read input from STDIN. Print output to STDOUT
s1 = raw_input()
s2 = raw_input()
count =0
for i in range (0, len(s1)-2) :
    if(s1[i:i+len(s2)]==s2) : count = count+1
print count