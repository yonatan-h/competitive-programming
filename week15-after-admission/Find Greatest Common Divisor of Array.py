class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)

        
        return get_gcd(min_, max_)



def get_gcd(big, small):

    while small > 0:
        remainder = big%small
        big = small
        small = remainder
    return big
