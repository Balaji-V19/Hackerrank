#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    rlen=len(arr[0])
    clen=len(arr)
    re=[]
    for i in range(rlen):
        for j in range(clen):
            if(i+2<rlen and j+2<clen):
                roadd=arr[i][j]+arr[i][j+1]+arr[i][j+2]
                nexadd=arr[i+1][j+1]
                lstadd=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                re.append(int(roadd)+int(nexadd)+int(lstadd))
                
    print(max(re))


