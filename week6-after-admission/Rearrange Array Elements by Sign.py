class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
                
        
        positives_turn = True
        for half_index in range(len(nums)//2):
            positive_index = half_index *2
            negative_index = positive_index + 1
            
            nums[positive_index] = positives[half_index]
            nums[negative_index] = negatives[half_index]
            
        return nums
    
#10min
#1sub
        