class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1

        #if negative
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            new_x = x*x
            new_n = n//2
            return self.myPow(new_x, new_n)
        else:
            new_n = n-1
            return x * self.myPow(x, new_n)


#25min
#2sub