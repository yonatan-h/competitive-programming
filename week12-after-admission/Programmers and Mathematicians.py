def get_max_groups(num_maths, num_progs):
    
    
    max_groups = max(num_maths, num_progs)
    
    larger = max(num_maths, num_progs)
    smaller = min(num_maths, num_progs)
    
    
    if larger > 3*smaller:
        #for each group there is 1 or 0 members of smaller
        return smaller
    else:
        #for each group there is be 1 or more members of smaller
        #join all of them, divide them to groups of 4
        #you can rearrange them so that there is >=1 member of smaller in each group
        
        return (smaller + larger)//4
        
        
def main():
    num_test_cases = int(input())
    
    for _ in range(num_test_cases):
        (num_maths, num_progs) = tuple(map(int, input().split()))
        print(get_max_groups(num_maths, num_progs))
        
main()

#4sub
#120min