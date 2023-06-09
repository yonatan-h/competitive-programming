class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool: 
        left = float("inf")
        middle = -float("inf")
        nums.append(nums[-1])
        is_fixed = False

        for i in range(len(nums)-1):
            cur = nums[i]
            nex = nums[i+1]

            if cur < nex and not is_fixed:
                left = cur
                middle = nex
                is_fixed = True

            if is_fixed:
                if cur < nex:
                    if cur < left and nex < middle:
                        left = cur
                        middle = nex
                    
                
                if cur > left and cur < middle:
                    middle = cur
                
                if cur > middle:
                    return True
            




            
            


        return False
            

