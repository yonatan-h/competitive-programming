class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        canceled_rows = set()
        canceled_cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    canceled_rows.add(row)
                    canceled_cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in canceled_rows or col in canceled_cols:
                    matrix[row][col] = 0
        