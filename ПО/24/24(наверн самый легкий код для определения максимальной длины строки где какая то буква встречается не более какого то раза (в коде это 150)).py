s = open('24.txt').readline()[:-1]
a = [i for i in range(len(s)) if s[i]=='Y']
maxl = 0
for i in range(150,len(a)):
    maxl = max(a[i]-a[i-150],maxl) 
    print(maxl)