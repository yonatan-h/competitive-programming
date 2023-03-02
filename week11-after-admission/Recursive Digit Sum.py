#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def get_super_digit(string_num):
    
    if len(string_num)==1:
        return int(string_num)
    
    sum_digits = 0
    for string_digit in string_num:
        sum_digits += int(string_digit)
    return get_super_digit(str(sum_digits))

def superDigit(n, k):
    #magically super_digit(abcd) == super_digit( super_digit(ab) + super_digit(cd)  )
    n_string = str(n)
    n_super_digit = get_super_digit(n_string)
    return get_super_digit(str(n_super_digit)*k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#30min
#1sub