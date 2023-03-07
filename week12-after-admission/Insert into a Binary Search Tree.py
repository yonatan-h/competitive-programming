# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        insert(root, val)
        return root

def insert(node, value):
    is_less = value < node.val
    is_more = value > node.val 

    #base case
    if is_less and node.left == None:
        node.left = TreeNode(value)
    elif is_more and node.right == None:
        node.right = TreeNode(value)

    #middle case
    elif is_less:
        insert(node.left, value)
    elif is_more:
        insert(node.right, value)
    

#1sub
#10min
