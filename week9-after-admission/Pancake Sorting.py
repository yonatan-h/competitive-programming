class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        return pancake_sort(arr)
        
def pancake_sort(nums):
    ks = []
    for right in reversed(range(len(nums))):
        max_index = find_max_index(right, nums)
        
        k_first = max_index+1
        flip(max_index, nums)
        
        k_second = right+1
        flip(right, nums)
        
        ks.append(k_first)
        ks.append(k_second)
    return ks

        

def flip(index, nums):
    for i in range(1+index//2):
        left = i
        right = index - i
        
        nums[left], nums[right] = nums[right], nums[left]

def find_max_index(right_most_index, nums):
    max_index = 0
    for i in range(right_most_index+1):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index
        
#30min
#1sub