class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subsets = [[]]
        self.form_subset([], 0)
        return self.subsets

    def form_subset(self, subset, index):
        for i in range(index, len(self.nums)):
            subset.append(self.nums[i])
            self.subsets.append(subset[:])
            self.form_subset(subset, i+1)
            subset.pop()

#20min
#1sub