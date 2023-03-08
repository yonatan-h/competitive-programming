# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', lesser_target: 'TreeNode', greater_target: 'TreeNode') -> 'TreeNode':
        if lesser_target.val > greater_target.val:
            lesser_target, greater_target = greater_target, lesser_target
        
        lesser_on_left = lesser_target.val <= node.val
        greater_on_right = greater_target.val >= node.val
        
        if lesser_on_left and greater_on_right:
            return node

        elif lesser_on_left: #both on left
            return self.lowestCommonAncestor(node.left, lesser_target, greater_target)
        else: #both on right
            return self.lowestCommonAncestor(node.right, lesser_target, greater_target)

#40min
#2sub

    







