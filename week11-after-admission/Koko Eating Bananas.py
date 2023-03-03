class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #speed from 1 to max(piles)
        min_speed = 0
        max_speed = max(piles)

        while max_speed > min_speed + 1:
            middle_speed = min_speed + (max_speed-min_speed)//2

            if can_finish(middle_speed, h, piles):
                max_speed = middle_speed
            else:
                min_speed = middle_speed
        
        return max_speed

    


def can_finish(speed, max_hours, piles):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile/speed)

    return hours <= max_hours

#20min
#1sub
