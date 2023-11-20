# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return node
        
        node.left, node.right = node.right, node.left
        self.invertTree(node.left)
        self.invertTree(node.right)
        return node
        