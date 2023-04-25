class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        col2 = 0
        col1 = 0

        for num in nums:
            col2, col1 = rem_3(col2, col1, abs(num))
        
        #col1 is actually abs(ans)
        num_positives = 0
        for num in nums:
            if num == col1: num_positives += 1
        
        if num_positives == 1:
            return col1
        else:
            return -col1

        


def rem_3(col2, col1, col0):
    #overflows are thrown out
    res_col1 = 0
    res_col2 = 0

    for shifts in range(33):
        mask = 1 << shifts
        val_0 = 1 if col0 & mask > 0 else 0
        val_1 = 1 if col1 & mask > 0 else 0
        val_2 = 1 if col2 & mask > 0 else 0

        sum = val_0 + val_1 + val_2
        
        res_col1 &= ~mask
        res_col2 &= ~mask

        if sum == 1:
            res_col1 = mask | res_col1
        elif sum == 2:
            res_col1 = mask | res_col1
            res_col2 = mask | res_col2
        #if summ == 0 or sum == 3: keep em zero`
    return (res_col2, res_col1)


            
