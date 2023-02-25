class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        
        #build prefix sum
        for num in nums:
            running_sum = prefix_sums[-1] + num
            prefix_sums.append(running_sum)
        
        
    
        remainder_counts = defaultdict(int)
        num_sub_arrays = 0
        
        for prefix_sum in prefix_sums:
            
            needed_remainder = prefix_sum % k
            num_windows = remainder_counts[needed_remainder]
            num_sub_arrays += num_windows
            
            remainder_counts[prefix_sum%k] += 1
            
                
        
        return num_sub_arrays
    
#20min
#1sub