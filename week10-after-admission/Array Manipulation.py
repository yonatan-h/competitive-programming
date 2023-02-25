#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
     
        

def find_max_num(change_indexes, changes):
    max_num = -float("inf")
    running_sum = 0
    for i in change_indexes:
        running_sum += changes[i]
        num = running_sum
        max_num = max(max_num, num)
    
    return max_num
            
        
        

def compress_queries(queries):
    compressed_query = defaultdict(int)
        
    for query in queries:
        start_index = query[0]
        end_index = query[1]+1
        steps = query[2]
            
        compressed_query[start_index] += steps
        compressed_query[end_index] -= steps
            
    return compressed_query
    
def get_change_indexes(queries):
    changes = []
    for query in queries:
        changes.append(query[0])
        changes.append(query[1]+1)
    changes.sort()
    return changes

def arrayManipulation(n, queries):
    compressed_query = compress_queries(queries)
    
    change_indexes = list(compressed_query.keys())
    change_indexes.sort()
    
    max_num = float('-inf')
    running_sum = 0
    for change_index in change_indexes:
        running_sum += compressed_query[change_index]
        max_num = max(max_num, running_sum)
    
    return max_num

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

#60min
#6sub