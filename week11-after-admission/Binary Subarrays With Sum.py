class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1 #for considering array from 0 upto ith element
        running_sum = 0
        num_sub_arrays = 0

        for num in nums:
            running_sum += num

            needed_prefix_sum = running_sum - goal
            num_sub_arrays += prefix_sum_counts[needed_prefix_sum]

            prefix_sum_counts[running_sum] += 1
        
        return num_sub_arrays

#15min
#1sub
