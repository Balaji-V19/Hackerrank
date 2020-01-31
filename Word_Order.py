
n=int(input())
di={}
for i in range(n):
    wor=input()
    if(wor in di):
        di[wor]+=1
    else:
        di[wor]=1
print(len(di))

for i,j in di.items():
    print(j,end=' ')
