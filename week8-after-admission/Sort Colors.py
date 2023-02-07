class Solution:
    def sortColors(self, nums: List[int]) -> None:
        selectionSort(nums, len(nums))

        
def select( arr, left):
    min_index = left
    for i in range(left, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index
                
                
    
def selectionSort(arr,n):
    for i in range(n):
        min_index = select(arr, i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

#3min
#1sub