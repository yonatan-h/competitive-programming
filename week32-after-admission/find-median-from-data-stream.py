class MedianFinder:

    def __init__(self):
        self.small_nums = []
        self.big_nums = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small_nums, -num)
        #transfer the biggest num from left side
        heappush(self.big_nums,  -heappop(self.small_nums))
        #transfer the smallest num from right side
        heappush(self.small_nums,  -heappop(self.big_nums))

        #keep the two sides equal
        if len(self.small_nums) > len(self.big_nums)+1:
            heappush(self.big_nums,  -heappop(self.small_nums))


        
    def findMedian(self) -> float:
        is_even = (len(self.small_nums) + len(self.big_nums))%2 == 0
        if is_even:
            median = (-self.small_nums[0] + self.big_nums[0])/2
            return median
        else:
            #small_nums are always filled before the big_nums
            return -self.small_nums[0]




        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()