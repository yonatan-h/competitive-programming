# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.col_row_values = defaultdict(list)
        self.traverse_append(0,0,root)

        cols = list(self.col_row_values.items())
        cols.sort()
        
        answer = []

        for i in range(len(cols)):
            (col, row_value_pairs) = cols[i]
            row_value_pairs.sort()

            column = []
            for j in range(len(row_value_pairs)):
                (row, value) = row_value_pairs[j]
                column.append(value)
            answer.append(column)
        
        return answer


    def traverse_append(self, row, col, node):
        if node is None:
            return

        self.col_row_values[col].append((row, node.val))
        self.traverse_append(row+1, col-1, node.left)
        self.traverse_append(row+1, col+1, node.right)