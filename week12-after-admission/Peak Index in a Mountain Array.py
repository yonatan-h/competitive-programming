class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return search_peak(arr)


def is_down_slope(nums, index):
    return nums[index] > nums[index+1]

def search_peak(nums):
    left = 0 #up slope
    right = len(nums)-2 #down slope

    while right > left + 1:
        mid = (left + right)//2

        if is_down_slope(nums, mid):
            right = mid
        else:
            left = mid

    return right


#30min
#1sub
