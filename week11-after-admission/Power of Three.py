

        
class Solution:
    def isPowerOfThree(self, target_num: int) -> bool:
        if target_num < 0:
            return False
        
        return is_power_of_three(1, target_num)




def is_power_of_three(cur_num, target_num):
    if cur_num == target_num:
        return True
    elif cur_num > target_num:
        return False
    
    next_num = cur_num*3
    return is_power_of_three(next_num, target_num)

#5min
#1sub