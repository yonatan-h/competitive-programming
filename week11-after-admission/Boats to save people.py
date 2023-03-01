class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_trips = 0
        left = 0
        right = len(people)-1
        
        while left <= right:
            at_right = people[right]
            at_left = people[left]
            
            if at_left + at_right > limit:
                num_trips += 1
                right -= 1
            else:
                num_trips += 1
                left += 1
                right -= 1
        return num_trips
                
#20min
#4sub