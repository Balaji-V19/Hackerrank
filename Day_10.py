#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bi=format(n,'b')
    co=0
    res=0
    for i in range(len(bi)):
        if(bi[i]=='0'):
            co=0
        else:
            co+=1
            res=max(res,co)      
    print(res)          
