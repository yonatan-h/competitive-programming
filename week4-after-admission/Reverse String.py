class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            left = i
            right = len(s)-1-i
            
            s[left],s[right] = s[right], s[left]
        
#7min
#2sub