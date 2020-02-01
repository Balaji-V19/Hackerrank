# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

ip=input().split()
va=list(permutations(ip[0],int(ip[1])))
ls=[]
for i in range(len(va)):
    st=""
    for j in range(int(ip[1])):
        st+=str(va[i][j])
    ls.append(st)
ls.sort()    
for i in range(len(ls)):
    print(ls[i])        
