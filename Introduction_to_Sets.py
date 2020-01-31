def average(array):
    le=len(set(array))
    ls=list(set(array))
    va=0
    for i in range(le):
        va+=ls[i]
    res=va/le
    return res   


    # your code goes here

if __name__ == '__main__':
