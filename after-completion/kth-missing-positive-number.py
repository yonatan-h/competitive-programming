class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = 0
        arr = deque(arr)
        for num in range(1, 2001):
            if arr and arr[0] == num:
                arr.popleft()
            else:
                missing += 1
                if k == missing:
                    return num
        

        



        