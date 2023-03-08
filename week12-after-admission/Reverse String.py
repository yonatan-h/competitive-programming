class Solution:
    def reverseString(self, s: List[str]) -> None:
        swap(s, 0, len(s)-1)

def swap(letters, left, right):
    if left < right:
        letters[left], letters[right] = letters[right], letters[left]
        swap(letters, left+1, right-1)

#30min
#3sub