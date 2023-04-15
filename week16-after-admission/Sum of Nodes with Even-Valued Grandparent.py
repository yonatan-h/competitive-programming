# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum_ = 0
        self.traverse(root, False, False)
        return self.sum_

    def traverse(self, node, is_even_parent, is_even_grand):
        if node is None:
            return
        
        am_even = node.val%2==0
        if is_even_grand: self.sum_ += node.val

        self.traverse(node.left, am_even, is_even_parent)
        self.traverse(node.right, am_even, is_even_parent)
