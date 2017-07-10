# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
n = int(n)
arr = list()
while (n>0) :
    p = raw_input()
    if "insert" in p :
        a = p[7]
        b = p[9:]
        a = int(a)
        b = int(b)
        arr.insert(a,b)
    elif "remove" in p :
        a = p[7:]
        a = int(a)
        arr.remove(a)
    elif "append" in p :
        a = p[7:]
        a = int(a)
        arr.append(a)
    elif "sort" in p :
        arr.sort()
    elif "pop" in p :
        t = arr.pop()
    elif "reverse" in p :
        arr.reverse()
    elif "print" in p :
        print arr
    n = n-1