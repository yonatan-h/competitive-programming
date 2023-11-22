class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indexes = defaultdict(lambda: [inf, -inf])
        counts = defaultdict(int)

            
        for i in range(len(nums)):
            num = nums[i]
            counts[num] += 1
            indexes[num][0] = min(i, indexes[num][0])
            indexes[num][1] = max(i, indexes[num][1])
        
        max_num = nums[0]
        max_range = inf

        for num in nums:
            first_i, last_i = indexes[num]
            range_num = last_i - first_i +1

            better_count = counts[num] > counts[max_num]
            same_count = counts[num]==counts[max_num]
            better_range = range_num < max_range

            if better_count or (same_count and better_range):
                max_num = num
                max_range = range_num

        return max_range

        