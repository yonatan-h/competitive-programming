class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        return sum_even_after_queries(nums, queries)
        
def is_even(nums):
    return nums%2 == 0

def sum_even_after_queries(nums, queries):
    current_sum = 0
    for num in nums:
        if is_even(num):
            current_sum += num
    
    print(current_sum)
    even_sum_after_queries = []
    for query in queries:
        added_value, index = query
        
        queried_num = nums[index]
        nums[index] += added_value
        after_query_num = nums[index]
        
        if is_even(queried_num):
            current_sum -= queried_num            
        
        if is_even(after_query_num):
            current_sum += after_query_num
        
            
        even_sum_after_queries.append(current_sum)
    
    return even_sum_after_queries

#1sub
#25min