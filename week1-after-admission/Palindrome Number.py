class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.stringIsPalindrome(str(x))

    def stringIsPalindrome(self, string):
        length = len(string)
        for i in range(length):
            left = string[i]
            right = string[length-1-i]
            if left != right: return False
        return True
#10min