class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = Counter(nums)
        operations_count = 0

        for num in list(set(nums)):
            gap_num = k - num

            if gap_num == num:
                #~half add with ~half
                half_count = num_count[num]//2

                num_count[num] -= half_count
                operations_count += half_count

            else:
                min_count = min(num_count[num], num_count[gap_num])
                
                num_count[num] -= min_count
                num_count[gap_num] -= min_count
                operations_count += min_count
        return operations_count

#15min
#1sub