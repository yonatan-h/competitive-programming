class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [None]*(3 + n+1)

        nums[0] = 0
        nums[1] = 1
        nums[2] = 1

        def explore(i):
            print(i)
            half_i = i//2
            next_to_half = half_i+1

            if nums[half_i] is None:
                explore(half_i)
            if nums[next_to_half] is None:
                explore(next_to_half)
            
            if i%2 == 0:
                nums[i] = nums[half_i]
            else:
                nums[i] = nums[half_i] + nums[next_to_half]
        
        for i in reversed(range(len(nums))):
            explore(i)

        return max(nums[:n+1])