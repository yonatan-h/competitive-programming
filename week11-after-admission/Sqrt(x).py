class Solution:
    def mySqrt(self, x: int) -> int:
        min_num = 0
        max_num = x+1

        while max_num > min_num + 1:
            middle_num = (min_num + max_num)//2

            if middle_num * middle_num > x:
                max_num = middle_num
            else:
                min_num = middle_num

        return min_num
#10min
#3sub
