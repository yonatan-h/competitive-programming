def main():
    len_nums, len_sets = input_number_list()
    nums = input_number_list()
    set_a = set(input_number_list())
    set_b = set(input_number_list())

    happiness = 0
    for num in nums:
        if num in set_a:
            happiness += 1
        if num in set_b:
            happiness -= 1
    
    print(happiness)

def input_number_list():
    return list(map(int, input().split()))

main()

#1sub
#10min
