# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rights = defaultdict(int)
        self.save_right(0,root)

        row_value_pairs = list(self.rights.items())
        row_value_pairs.sort()
        values = []
        for (row, value) in row_value_pairs:
            values.append(value)
        return values


    
    def save_right(self, row, node):
        if node == None:
            return
        
        self.rights[row] = node.val
        
        #go left first, 
        self.save_right(row+1, node.left)
         #go right
        self.save_right(row+1, node.right)
