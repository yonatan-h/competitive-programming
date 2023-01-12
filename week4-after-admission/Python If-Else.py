#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    is_odd = n%2 != 0
    is_even = n%2 == 0
    in_2_to_5 = 2 <= n <= 5
    in_6_to_20 = 6 <= n <= 20
    greater_than_20 = n > 20
    
    weird = "Weird"
    not_weird = "Not Weird"
    
    if (is_odd): print(weird)
    if (is_even and in_2_to_5): print(not_weird)
    if (is_even and in_6_to_20): print(weird)
    if (is_even and greater_than_20): print(not_weird)
    
    #5min
    #1sub
