# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return get_max_height(root)


def get_max_height(node):
    if node == None:
        return 0

    including_left = get_max_height(node.left)
    including_right = get_max_height(node.right)

    return max(including_left, including_right) +1 
 
#15min
#4sub
