
def firstMissingPositive(nums):
    for i in range(len(nums)):

        while should_swap(i, nums[i]-1, nums):
            place = nums[i]-1
            nums[i], nums[place] = nums[place], nums[i]
    
    for i in range(len(nums)):
        if i != nums[i]-1:
            return i+1

    return nums[-1]+1



def should_swap(fro, to, nums):
    #destination should be inbound
    if not 0 <= to < len(nums): return False
    if nums[fro]-1 == to: return False
    return True


print(firstMissingPositive([1,1]))
    
    

