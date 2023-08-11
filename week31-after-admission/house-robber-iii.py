# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def steal(node, can_rob):
                #also try robbing option
            if can_rob:
                left_money = steal(node.left, False)
                right_money = steal(node.right, False)
                robbed = node.val + left_money + right_money
            
            #skip option
            robbed = 0
            left_money = steal(node.left, True)
            right_money = steal(node.right, True)
            robbed = max(robbed, left_money + right_money)
            
            if node == None:
                return 0
        
        return steal(root, True)
            return robbed