# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return choose(root, val)

def choose(node, target):
    if node == None:
        return None
    
    if target < node.val:
        return choose(node.left, target)
    elif target > node.val:
        return choose(node.right, target)
    return node

#10min
#1sub