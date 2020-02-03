# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
di=dict()
for i in range(n):
    bj,ls=input().split()
    di[bj]=ls
td=[]    
for i in range(n):
    td.append(input())
for i in range(n):
    if(td[i] in di):
        print(td[i]+'='+di[td[i]])
    else:
        print('Not found')    
        
       

