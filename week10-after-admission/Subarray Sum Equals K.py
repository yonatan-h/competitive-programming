class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = [0]
        
        #build prefix sum
        for num in nums:
            running_sum = prefix_sums[-1] + num
            prefix_sums.append(running_sum)
        
        
    
        prefix_counts = defaultdict(int)
        num_sub_arrays = 0
        
        for prefix_sum in prefix_sums:
            
            needed_sum = prefix_sum - k
            num_windows = prefix_counts[needed_sum]
            num_sub_arrays += num_windows
            
            prefix_counts[prefix_sum] += 1
            
                
        
        return num_sub_arrays
    
#35min
#2sub