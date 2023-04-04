from math import log2
 
 
 
def satisfies(x,y):
    return x&y > 0 and x^y > 0
    
def find_y(x):
 
    length = int(log2(x))
 
    and_respecter = 1
    while True:
        if x&and_respecter > 0: break
        else: and_respecter <<= 1
    
    xor_respecter = 1
    while True:
        if x^xor_respecter > 0: break
        else: xor_respecter <<= 1
 
    
    and_satisfies = satisfies(x, and_respecter)
    xor_satisfies = satisfies(x, xor_respecter)
 
    if and_satisfies and xor_satisfies:
        return min(xor_respecter, and_respecter)
    elif and_satisfies:
        return and_respecter
    elif xor_satisfies:
        return xor_satisfies
    else:
        return xor_respecter + and_respecter
 
 
num_test_cases = int(input())
 
for _ in range(num_test_cases):
    x = int(input())
    print(find_y(x))