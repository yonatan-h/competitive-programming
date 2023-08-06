class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in reversed(range(len(arr)-1)):
            smaller_i = -1
            for j in range(i+1, len(arr)-1):
                if arr[smaller_i] < arr[j] < arr[i]:
                    smaller_i = j
            if smaller_i != -1:
                arr[i], arr[smaller_i] = arr[smaller_i], arr[i]
                break
        
        return arr
        arr.append(-1)
        arr.pop()