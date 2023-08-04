class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        layer = [poured]
        for _ in range(query_row):
            beneath = [0]*(len(layer)+1)
            for i in range(len(layer)):
                top_glass = layer[i]
                if over_flowed < 0: over_flowed = 0
                beneath[i] += 0.5*over_flowed
            layer= beneath
        
                over_flowed = top_glass - 1
                beneath[i+1] += 0.5*over_flowed
        if layer[query_glass]>=1:
            return 1
        else:
            return layer[query_glass]