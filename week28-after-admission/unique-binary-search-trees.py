class Solution:
    def numTrees(self, n: int) -> int:
        #num_nodes -> num_unique_bsts
        shortcuts = {
            #0 neighbors to left or right == None is place taker
            0:1, 
            1:1, 
        }

        for length in range(1, n+1):
            
            num_uniques = 0
            for mid in range(length):
                #mid is not included
                left_len = mid
                right_len = length-1 - mid

                num_uniques += shortcuts[left_len] * shortcuts[right_len]

            shortcuts[length] = num_uniques
        
        return shortcuts[n]







