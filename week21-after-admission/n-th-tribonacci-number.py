class Solution:
    def tribonacci(self, n: int) -> int:
        
        first = 0
        second = 1
        third = 1

        if n == 0: return first
        elif n == second: return second
        elif n == third: return third

        for i in range(n-2):
            new_third = first + second + third
            first = second
            second = third
            third = new_third

        return third
