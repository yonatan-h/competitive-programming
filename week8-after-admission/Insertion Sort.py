#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    off_num = arr[-1]
    if n <= 1: return 

    for i in reversed(range(n-1)):
        if arr[i] >= off_num:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = off_num
            print(*arr)
            return
    arr[0] = off_num
    print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
#1sub
#20min