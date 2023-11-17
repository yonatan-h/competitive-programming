class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return find_adders(target, nums)

def find_adders(target, nums):
    num_indexes_map = defaultdict(list)
    
    for i in range(len(nums)):
        num = nums[i]
        num_indexes_map[num].append(i)
    
    for num_index in range(len(nums)):
        num = nums[num_index]
        num_needed = target - num
        
        needed_indexes = num_indexes_map[num_needed]
        
        #empty list == needed_num does not exist
        
        for needed_index in needed_indexes:
            if needed_index != num_index:
                return [num_index, needed_index]
