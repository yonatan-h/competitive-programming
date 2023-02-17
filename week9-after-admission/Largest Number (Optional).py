class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return get_largest_num(nums)
        
def get_largest_num(nums):
    string_nums = list(map(str, nums))
    mod_bubble_sort(string_nums)
    joined =  "".join(string_nums)
    is_zero = joined[0] == "0" #biggestish number is zero
    
    if is_zero:
        return "0"
    else:
        return joined
    
    
    

    
def mod_bubble_sort(string_nums):
    length = len(string_nums)
    for left in range(length):
        for i in reversed(range(left, length-1)):
            curr_num = string_nums[i]
            next_num = string_nums[i+1]
            
            if next_num + curr_num > curr_num + next_num:
                string_nums[i+1] = curr_num
                string_nums[i] = next_num
    
                
                
        

#30min
#3sub