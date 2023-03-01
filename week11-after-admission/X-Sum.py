from collections import defaultdict
 
def get_max_attacks(matrix):
    up_diags = defaultdict(int)
    down_diags = defaultdict(int)
 
    #fill up diags
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            up_diags[row+col] += matrix[row][col]
 
    #fill down diags
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            down_diags[row-col] += matrix[row][col]
 
    #find best position
    max_sum = -float("inf")
 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            up_diag = row + col
            down_diag = row - col
 
            sum = up_diags[up_diag] + down_diags[down_diag] - matrix[row][col]
            if sum > max_sum:
                max_sum = sum
    
    return max_sum
 
 
    
def main():
    num_test_cases = int(input())
 
    for _ in range(num_test_cases):
        [height, width] = list(map(int, input().split()))
        matrix = []
        for __ in range(height):
            row = list(map(int, input().split()))
            matrix.append(row)
        print(get_max_attacks(matrix))
 
 
main()

#60min
#1sub