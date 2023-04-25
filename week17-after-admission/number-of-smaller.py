def bisect_left(nums, inserted):
    left = -1 #< inserted
    right = len(nums) #>= inserted

    while left+1 != right:
        mid = (left+right)//2
        if nums[mid] < inserted:
            left = mid
        else:
            right = mid
    
    return left

_ = input()
nums = list(map(int, input().split()))
inserteds = list(map(int, input().split()))
for inserted in inserteds:
    print(bisect_left(nums, inserted)+1, end=" ")



