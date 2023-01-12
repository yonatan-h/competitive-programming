class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_slots = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        slot_index = carType-1
        self.parking_slots[slot_index] -= 1
        
        remaining_slots = self.parking_slots[slot_index]
        if remaining_slots >= 0: return True
        else: return False

#1sub
#7min
        
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)