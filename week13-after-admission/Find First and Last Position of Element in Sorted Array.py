class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left_validator(num):
            return num >= target
        def bisect_right_validator(num):
            return num > target
        
        first = binary_search(nums, bisect_left_validator)
        last = binary_search(nums, bisect_right_validator)-1

        #if no first, there is no last
        first_in_range = 0 <= first< len(nums)
        if not first_in_range:
            return [-1,-1]
        elif not nums[first] == target:
            return [-1,-1]
        else:
            return [first, last]
        

        


        


def binary_search(nums, is_good):
    left = -1
    right = len(nums)

    while right > left + 1:
        mid = (left + right)//2
        if is_good(nums[mid]):
            right = mid
        else:
            left = mid
    

    return right

#10min
#1sub



