def get_less_or_equal(loe_length, nums):
    nums.sort()
    if loe_length == 0:
        if nums[0] > 1:
            return 1
        else:
            return -1
        
    
    nums.append(float("inf")) #dummy number
    index = loe_length - 1
    num = nums[index]

    if nums[index+1] == num:
        return -1
    else:
        return num

def main():
    [nums_length, loe_length] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(get_less_or_equal(loe_length, nums))

main()

#2sub
#30min