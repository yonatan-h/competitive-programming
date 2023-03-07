class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]: 
        for i in range(len(intervals)):
            intervals[i] = (intervals[i], i)

        intervals.sort()
        right_indexes = [None]*len(intervals)
        for interval in intervals:
            right_index = find_right_index(interval, intervals)
            index = interval[1]
            right_indexes[index] = right_index
        return right_indexes
        

def find_right_index(interval, intervals):
    left = -1
    right = len(intervals)

    while right > left + 1:
        mid = (left + right)//2
        if is_right(interval, intervals[mid]):
            right = mid
        else:
            left = mid
    
    if right == len(intervals):
        return -1
    else:
        return intervals[right][1]

    
def is_right(left_interval, right_interval):
    [start_left, end_left] = left_interval[0]
    [start_right, end_right] = right_interval[0]

    return start_right >= end_left

 #30min
#1sub
