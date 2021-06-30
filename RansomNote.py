 	#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    cnt = 0
    mag = sorted(magazine)
    nt = sorted(note)
    for i in nt:
        if i in mag:
            cnt = cnt +1  
            mag.remove(i)    
        else:
            break 
    if cnt == n:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
