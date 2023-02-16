class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return count_distinct(nums)

        
def count_distinct(nums):
    length = len(nums)
    for i in range(length):
        num = nums[i]
        nums.append(reverse(num))
    
    return len(set(nums))
        

def reverse(num):
    digits = list(str(num))
    reversed_digits = list(reversed(digits))
    reversed_num = int("".join(reversed_digits))
    return reversed_num

#1sub
#10min
    
    