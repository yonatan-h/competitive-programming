class DataStream:

    def __init__(self, value: int, k: int):
        self.smooth_count = 0
        self.k = k
        self.value = value
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.smooth_count += 1
        else:
            self.smooth_count = 0
        
        return self.smooth_count >= self.k
        


#5min
#1sub