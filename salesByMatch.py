#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pair = 0
    a=[]
    for i in range(n):
        if ar[i] not in a:
                a.append(ar[i])
    for i in a:
        count=0
        for j in range(n):
            if i==ar[j]:
                count = count+1
        if count%2 == 0:
            pair = pair + count//2
        else:
            pair = pair + (count-1)//2
            
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

