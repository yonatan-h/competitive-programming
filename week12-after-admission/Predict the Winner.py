class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        smart_score = smart_play(True, 0, len(nums)-1, nums)
        return smart_score >= 0



#positive score is good for player1, negative is good for player2
def smart_play(is_turn1, left, right, nums):

    if left + 1 == right:
        #play last two rounds (clear to choose the best route)
        best_score = abs(nums[right]-nums[left])
        if is_turn1:
            return best_score
        else:
            return -best_score
    

    if is_turn1:
        left_gain = smart_play(False, left+1, right, nums) + nums[left]
        right_gain = smart_play(False, left, right-1, nums) + nums[right]
        return max(left_gain, right_gain)
    else:
        left_gain = smart_play(True, left+1, right, nums) - nums[left]
        right_gain = smart_play(True, left, right-1, nums) - nums[right]
        return min(left_gain, right_gain)

    
#60min
#9sub




        

