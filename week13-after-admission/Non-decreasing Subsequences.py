class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.sols = set()
        self.nums = nums

        self.generate(-1, [])
        return list(map(list, self.sols))
    
    def generate(self, last_added_index, arr):
        if len(arr) > 1:
            self.sols.add(tuple(arr))
        
        for i in range(last_added_index+1, len(self.nums)):
            if not arr or self.nums[i] >= arr[-1]:
                arr.append(self.nums[i])
                self.generate(i, arr)
                arr.pop()
