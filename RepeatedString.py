#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    st = list(s)
    count =0
    times=n//len(st)
    if n%len(st)==0:
        for i in range(len(st)):
            if st[i]=="a":
                count=count+1
        count = count*times
    else:
        for i in range(len(st)):
            if st[i]=="a":
                count=count+1
        count = count*times
        for j in range(n-len(st)*times):
            if st[j]=="a":
                count=count+1
    return count
    
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

