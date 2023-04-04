class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return count_ones(x^y)


def count_ones(num):
    count = 0
    while num :
        last_digit = num & 1
        count += last_digit
        num = num >> 1
    return count