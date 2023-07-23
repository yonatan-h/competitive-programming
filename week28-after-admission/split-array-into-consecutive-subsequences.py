class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        #tuples of
        #1000-last-num-in-sub sequence, and len subsequence 
        #you get the biggest tail 1st, and the smalles sub sequence(greedy)
        heap = []

        for num in nums:

            poppeds = []
            while heap and -heap[0][0] == num:
                poppeds.append(heappop(heap))
                
            if heap and -heap[0][0] == num-1:
                top_inversed, top_length = heappop(heap)
                heappush(heap, (-num, top_length+1))
            else:
                heappush(heap, (-num, 1))
            
            for popped in poppeds:
                heappush(heap, popped)

        
        for inverse_tail, length in heap:
            if length < 3: return False
        
        
        return True

     