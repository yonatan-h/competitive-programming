class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)        
        length = len(nums)

        count_nums = []

        for unique_num in counter:
            count = counter[unique_num]
            count_nums.append((count, unique_num))

        count_nums.sort()
        count_nums.reverse()

        nums = []
        for count, num in count_nums:
            nums.append(num)
        return nums[:k]


def parallel_sort(nums, parallel):
    for i in range(len(nums)):
        # nums[i] not where it needs to be (i)
        # nums[where it needs to be] != nums[i]
        while nums[i] != i+1 and  nums[i] != nums[nums[i]-1]:
            dest = nums[i]-1
            nums[i], nums[dest] = nums[dest], nums[i]
            parallel[i], parallel[dest] = parallel[dest], parallel[i]
