class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shifted_less = n >> 1
        length = int(log2(n))

        next_power = 1 << (length+1)
        return shifted_less+n+1 == next_power
