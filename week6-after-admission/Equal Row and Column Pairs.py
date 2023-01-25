class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return get_equal_pairs(grid)

    
def get_equal_pairs(matrix):
    rows = matrix
    columns = get_all_columns(matrix)
    
    return find_num_matches(rows, columns)


def get_all_columns(matrix):
    columns = []
    
    for  col_num in range(len(matrix)):
        column = []
        for row_num in range(len(matrix)):
            value = matrix[row_num][col_num]
            column.append(value)
        columns.append(column)
    return columns
            
        
def find_num_matches(rows, columns):
    match_count = 0
    for row in rows:
        for column in columns:
            if row == column:
                match_count+=1

    return match_count


#10min
#1sub