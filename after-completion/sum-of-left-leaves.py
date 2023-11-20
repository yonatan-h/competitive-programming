# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0

        def dfs(node, is_left):
            nonlocal left_sum
            if node is None: return
            if is_left and not (node.left or node.right):
                left_sum += node.val
            
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return left_sum
        

        