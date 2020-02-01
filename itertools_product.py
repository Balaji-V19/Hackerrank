# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
n=list(map(int,input().split()))
m=list(map(int,input().split()))
ls=list(product(n,m))
for i in range(len(ls)):
    print(ls[i],end=" ")
