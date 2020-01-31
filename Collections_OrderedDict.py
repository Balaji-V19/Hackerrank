# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

di=OrderedDict()
n=int(input())
for i in range(n):
    v=input().split(' ')
    if(len(v)>2):
        nu=v[2]
        wo=v[0]+" "+v[1]
    else:
        nu=v[1]
        wo=v[0]
    if(wo in di):
        di[wo]+=int(nu)
    else:
        di[wo]=int(nu)
for i,j in di.items():
    print(i+" "+str(j))            
