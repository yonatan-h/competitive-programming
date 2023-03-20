# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #all node counts, most recent count when a healthy node was added
        self.ends= defaultdict(lambda : [float("inf"), -float("inf")])
        self.save_width(0,0, root)

        max_width = 1
        for row in self.ends.keys():
            (left, right) = self.ends[row]
            max_width = max(right-left+1, max_width)

        return max_width
    
    def save_width(self, row, index, node):
        if node == None:
            return
        
        #update row ends
        (row_left, row_right) = self.ends[row]
        if index < row_left:
            self.ends[row][0] = index
        elif index > row_right:
            self.ends[row][1] = index

        #continue traversing
        left_index = index*2
        right_index = left_index+1

        self.save_width(row+1, left_index, node.left)
        self.save_width(row+1, right_index, node.right)


        


        






