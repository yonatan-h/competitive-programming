# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.build_string(root)

    
    def build_string(self, node):
        if node is None:
            return
        
        left_string = self.build_string(node.left)
        right_string = self.build_string(node.right)

        if not left_string and not right_string:
            return str(node.val)
        elif not right_string:
            return f"{node.val}({left_string})"
        elif not left_string:
            return f"{node.val}()({right_string})"
        else:#both not empty or left == "()"
            return f"{node.val}({left_string})({right_string})"