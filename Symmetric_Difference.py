# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ls=input().split(" ")
m=int(input())
ls2=input().split(" ")
se1=list(set(ls).difference(set(ls2)))
se2=list(set(ls2).difference(set(ls)))
res=[]
for i in range(len(se1)):
    res.append(int(se1[i]))  
for j in range(len(se2)):
    res.append(int(se2[j])) 
res.sort()
for i in range(len(res)):
    print(res[i])     



    

