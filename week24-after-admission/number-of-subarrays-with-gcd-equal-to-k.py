class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def gcd(num1, num2):
            big = max(num1, num2)
            small = min(num1, num2)

            while small:
                mod = big%small
                big = small
                small = mod
            
            return big

        count = 0

        for i in range(len(nums)):
            running_gcd = nums[i]
            for j in range(i, len(nums)):
                running_gcd =  gcd(running_gcd, nums[j])
                if running_gcd == k:
                    count += 1
                elif running_gcd < k:
                    break
                


        return count