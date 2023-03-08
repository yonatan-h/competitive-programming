# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    up_steps = 0
    kth_value = None

    def kthSmallest(self, node: Optional[TreeNode], k: int) -> int:
        if node == None:
            return
        
        self.kthSmallest(node.left, k)

        self.up_steps += 1
        if self.up_steps == k:
            self.kth_value = node.val
        
        self.kthSmallest(node.right, k)
        if self.kth_value is not None:
            return self.kth_value
        
#70min
#3sub