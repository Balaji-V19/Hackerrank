# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
po=0
to=0
for i in range(n+1):
    ls=input().split()
    if(i==0):
        for j in range(len(ls)):
            if(ls[j]=='MARKS'):
                po=j 
    else:
        to+=int(ls[po])
arg=to/n
print("%.2f"%arg)  
