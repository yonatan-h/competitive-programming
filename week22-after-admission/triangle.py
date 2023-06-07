class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        shortests = defaultdict(lambda : float("inf"))
        shortests[(0,0)] = triangle[0][0]

        for row_num in range(len(triangle)-1):
            for col_num in range(len(triangle[row_num])):
                cost = shortests[(row_num, col_num)]

                
                down_left = (row_num+1, col_num)
                down_right = (row_num+1, col_num+1)

                if cost + triangle[row_num+1][col_num] < shortests[down_left]:
                    shortests[down_left] = cost + triangle[row_num+1][col_num]

                if cost + triangle[row_num+1][col_num+1] < shortests[down_right]:
                    shortests[down_right] = cost + triangle[row_num+1][col_num+1]
        
        last_row_num = len(triangle)-1
        costs = []
        for col_num in range(len(triangle[-1])):
            costs.append(shortests[last_row_num, col_num])
        return min(costs)
