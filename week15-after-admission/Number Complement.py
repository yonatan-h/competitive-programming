class Solution:
    def findComplement(self, num: int) -> int:
        biggest_2_power = int(log2(num))
        sum_with_complement = (1 << (biggest_2_power + 1)) - 1
        
        complement = sum_with_complement - num
        return complement

