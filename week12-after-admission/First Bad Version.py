# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return binary_search(n)

def binary_search(max_version):
    left = -1
    right = max_version #assuming the last version is always bad

    while right > left + 1:
        mid = (left + right)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid

    return right

#8min
#1sub
