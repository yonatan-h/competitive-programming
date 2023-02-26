class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odd_subarrays_count = 0
        
        cumulative_odd_count = defaultdict(int)
        cumulative_odd_count[0] = 1
        running_odd_count = 0
        
        for num in nums:
            if is_odd(num):
                running_odd_count += 1
            cumulative_odd_count[running_odd_count] += 1
            
            needed_count = running_odd_count - k
            odd_subarrays_count += cumulative_odd_count[needed_count]
        return odd_subarrays_count
        
            
            

def is_odd(num):
    return num % 2 != 0
        
#40min
#2sub
