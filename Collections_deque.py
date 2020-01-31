# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d=deque()
n=int(input())
for i in range(n):
    ls=[]
    ls=input().split(" ")
    if(ls[0]=='append'):
        d.append(ls[1])
    elif(ls[0]=='appendleft'):
        d.appendleft(ls[1])
    elif(ls[0]=='pop'):
        d.pop()
    elif(ls[0]=='popleft'):
        d.popleft()  
for i in range(len(d)):
    print(d[i],end=" ")       

