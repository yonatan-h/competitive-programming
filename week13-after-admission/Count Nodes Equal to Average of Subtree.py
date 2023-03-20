# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.sum_num_below(root)
        return self.count

    def sum_num_below(self, node):
        if node is None:
            return (0,0)
        
        (sum_left, num_left) = self.sum_num_below(node.left)
        (sum_right, num_right) = self.sum_num_below(node.right)

        sum_tree = sum_left + node.val + sum_right
        num_tree = num_left + 1 + num_right
        average = sum_tree//num_tree

        if node.val == average:
            self.count += 1
        return (sum_tree, num_tree)
        
        