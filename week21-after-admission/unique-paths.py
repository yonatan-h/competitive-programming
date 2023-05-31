class Solution:
    def uniquePaths(self, height: int, width: int) -> int:
        answer = make_matrix(width, height)
        for col in range(width):
            answer[-1][col] = 1
        
        for row in range(height):
            answer[row][-1] = 1
        
        for row in reversed(range(height-1)):
            for col in reversed(range(width-1)):
                answer[row][col] = answer[row+1][col] + answer[row][col+1]
        
        return answer[0][0]



def make_matrix(width, height):
    matrix = []
    for _ in range(height):
        row = [None]*width
        matrix.append(row)
    return matrix