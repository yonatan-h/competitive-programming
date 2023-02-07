class Solution: 
    def select(self, arr, left):
        min_index = left
        for i in range(left, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index
                
                
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_index = self.select(arr, i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
#5min
#1sub