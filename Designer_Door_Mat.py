# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
sl=1
dec=False
for i in range(int(n)):
    t=int(m)-sl*3
    for j in range(int(m)):
        if(j+1==int(m)):
            print('')    
        elif(i==(int(n)-1)/2):
            va=int((int(m)-7)/2)
            dec=True
            print(va*'-'+'WELCOME'+va*'-')
            break
        else:
            s=int((int(m)-(sl*3))/2)
            print(s*'-'+sl*'.|.'+s*'-')  
            break  
    if(dec):
        sl-=2
    else:
        sl+=2               

