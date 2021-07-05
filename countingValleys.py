#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    val=0
    count=0
    fl=0
    check = 0
    for i in range(steps):
        i = check
        if i > steps or i == steps:
            return count
        if path[i]=="U":
            val=val+1
            check = i+1
        elif path[i]=="D" and val==0:
            
            val=val-1
            for j in range(i+1,steps,1):
                if(path[j]=="D"):
                    val=val-1
                elif(path[j]=="U"):
                    val=val+1
                    #print(val)
                if val==0:  
                    count=count+1
                    
                    check = j+1
                    fl =1
                    break
            
            if(check==steps):
                return count
        elif path[i]=="D" and val!=0:
            val=val-1
            check = i+1
    return count           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

