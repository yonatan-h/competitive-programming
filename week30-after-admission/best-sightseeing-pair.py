class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_height = -float('inf')
        best_index = -1
        best_score = -float('inf')
        for i in range(len(values)):
            distorted_height = best_height - (i - best_index)
            if  values[i] > distorted_height:
                best_height = values[i]
                best_index = i
            score = (values[i]+best_height) - (i - best_index)
            best_score = max(score, best_score)
        
        return best_score