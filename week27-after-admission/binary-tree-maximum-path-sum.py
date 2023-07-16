# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")
        self.max_path(root)
        return self.max_sum

    def max_path(self, node):
        if node is None:
            return 0
        
        left = self.max_path(node.left) 
        right = self.max_path(node.right) 
        val = node.val

        self.max_sum = max(val, left+val, right+val, left+right+val, self.max_sum)
        return max(val, left+val, right+val)
        