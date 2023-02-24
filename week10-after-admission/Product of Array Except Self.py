class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumulative = build_cumulative(nums)
        reverse = build_reverse(nums)
        
        print(cumulative)
        print(reverse)
        
        for i in range(len(nums)):
            before = None
            if i == 0:
                before = 1
            else:
                before = cumulative[i-1]
                
            
            after = None
            if i == len(nums)-1:
                after = 1
            else:
                after = reverse[i+1]
            
            nums[i] = before*after
        
        return nums
            
            
        
        
        
            
       
    
def build_cumulative(nums):
    cumulative_products = [nums[0]]
    for i in range(1, len(nums)):
        running_product = cumulative_products[-1] * nums[i]
        cumulative_products.append(running_product)
    return cumulative_products
        
def build_reverse(nums):
    reverse = [None]*len(nums)
    running_reverse = 1
    for i in reversed(range(len(nums))):
        running_reverse *= nums[i]
        reverse[i] = running_reverse
    return reverse
        
    
            
#25min
#1sub
        
            
        