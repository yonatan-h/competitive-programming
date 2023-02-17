from collections import defaultdict

def get_letter_counts(grid):
    row_letter_counts = defaultdict(int)
    col_letter_counts = defaultdict(int)

    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            letter = grid[row_num][col_num]

            row_letter_pair = (row_num,letter)
            col_letter_pair = (col_num,letter)

            row_letter_counts[row_letter_pair] += 1
            col_letter_counts[col_letter_pair] += 1

    return [row_letter_counts, col_letter_counts]

def solve_puzzle(grid):
    [row_letter_counts, col_letter_counts] = get_letter_counts(grid)

    encrypted = ""
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            letter = grid[row_num][col_num]
            row_letter_pair = (row_num,letter)
            col_letter_pair = (col_num,letter)

            row_count = row_letter_counts[row_letter_pair]
            col_count = col_letter_counts[col_letter_pair]

            if row_count == 1 and col_count == 1:
                encrypted += letter
    return encrypted

def main():
    [height, width] = list(map(int, input().split()))
    rows = []

    for _ in range(height):
        rows.append(input())
    
    answer = solve_puzzle(rows)
    print(answer)

main()

#3sub
#40min