class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        return get_worst_case_p2_score(grid)


def get_worst_case_p2_score(grid):
    width = len(grid[0])

    #build score prefix sum
    running_to_right = 0
    for i in range(width):
        running_to_right += grid[0][i]
        grid[0][i] = running_to_right
    
    running_to_left = 0
    for i in reversed(range(width)):
        running_to_left += grid[1][i]
        grid[1][i] = running_to_left

    min_p2_score = float("inf")

    for i in range(width):
        p1_up_score = grid[0][i]
        p1_down_score = grid[1][i]

        #p2 either picks up or down
        p2_up_score = grid[0][width-1] - p1_up_score
        p2_down_score = grid[1][0] - p1_down_score

        optimal_p2_score = max(p2_up_score, p2_down_score)

        #we pick the best job done by p1
        min_p2_score = min(min_p2_score, optimal_p2_score)

    return min_p2_score

#30min
#1sub

    