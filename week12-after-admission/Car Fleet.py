class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        pos_speed_pairs = list(zip(positions, speeds))
        pos_speed_pairs.sort()

        cars = []
        for car in reversed(pos_speed_pairs):
            if cars and can_contact(car,cars[-1], target):
                pass
            else:
                cars.append(car)
            
        
        return len(cars)





def can_contact(car_behind, car, target_pos):
    (pos1, speed1) = car_behind
    (pos2, speed2) = car

    time1_to_target = (target_pos - pos1)/speed1
    time2_to_target = (target_pos - pos2)/speed2

    return time1_to_target <= time2_to_target

#2sub
#30min
