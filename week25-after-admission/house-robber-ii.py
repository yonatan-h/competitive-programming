class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        with_first = nums[0:-1]     
        with_last = nums[1:]
        return max(linear_rob(with_first), linear_rob(with_last))

def linear_rob(houses):
    houses = [0, 0]+houses
    answers= defaultdict(int)

    def rob(index):
        best_child = 0 
        if index >= len(houses):
            return
        if index in answers:
            return answers[index]
            
        for gap in (2,3):
            rob(index+gap)
            best_child = max(best_child, answers[index+gap])

        answers[index] = houses[index]+best_child 
    
    rob(0)
    return answers[0]


