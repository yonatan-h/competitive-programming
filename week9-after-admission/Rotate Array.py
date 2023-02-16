class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0: return
        
        index_first_element = (len(nums)-k)%len(nums)
        
        rotated_nums = []
        for i in range(index_first_element, index_first_element + len(nums)):
            
            cycling_i = i % len(nums)
            value = nums[cycling_i]
            rotated_nums.append(value)
            
        nums.clear()
        nums.extend(rotated_nums)
        return rotated_nums
            
#1sub
#15min