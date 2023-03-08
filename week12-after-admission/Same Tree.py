# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return is_same(p, q)



def is_same(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    
    if node1.val != node2.val:
        return False
    
    return is_same(node1.left, node2.left) and is_same(node1.right, node2.right)
    

#15min
#1sub