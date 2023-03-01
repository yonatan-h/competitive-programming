class Solution:
    def isPowerOfFour(self, target_num: int) -> bool:
        if target_num < 0:
            return False
        
        return is_power_of_four(1, target_num)




def is_power_of_four(cur_num, target_num):
    if cur_num == target_num:
        return True
    elif cur_num > target_num:
        return False
    
    next_num = cur_num*4
    return is_power_of_four(next_num, target_num)
#5min
#1sub