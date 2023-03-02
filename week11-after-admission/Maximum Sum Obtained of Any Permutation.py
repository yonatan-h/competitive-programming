class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        concentration_array = build_concentration_array(len(nums), requests)
        concentration_index_pairs = value_index_pairs(concentration_array)

        concentration_index_pairs.sort()
        nums.sort()

        #give max num to max concentration
        best_sum = 0
        for _ in range(len(nums)):
            (concentraion, index) = concentration_index_pairs.pop()
            max_num = nums.pop()

            best_sum += max_num * concentraion
            
        return best_sum % (10**9 + 7)
            

            


def value_index_pairs(nums):
    value_index_pairs = []
    for i in range(len(nums)):
        value_index_pairs.append((nums[i], i))
    return value_index_pairs


def build_concentration_array(length_nums, requests):
    changes = [0]*(length_nums+1)
    for request in requests:
        (start, end) = request
        changes[start] += 1
        changes[end+1] -= 1
    
    concentration_array = []

    running_sum = 0
    for change in changes:
        running_sum += change
        concentration_array.append(running_sum)
    
    return concentration_array
    
#25min
#1sub

