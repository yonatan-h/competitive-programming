class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #make zero indexed
        n -= 1
        k -= 1

        #as if the last row was a progress bar
        last_row_len = 2**n
        child_percent = k/last_row_len

        #at level zero
        window = "0"
        window_index = 0

        for level in range(n):
            #select ancestor from window
            row_len = 2**level
            ancestor_index = math.floor(row_len*child_percent)
            ancestor = window[ancestor_index - window_index]

            if ancestor == "0":
                window = "01"
            else:
                window = "10"
            window_index = ancestor_index*2
        
        child = window[k-window_index]
        return int(child)



#2sub



