# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    st=input()
    ev=''
    od=''
    for j in range(len(st)):
        if(j%2==0):
            ev+=st[j]
        else:
            od+=st[j]
    print(ev,od)            


