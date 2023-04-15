# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.path_sum = 0
        self.path = []
        self.search(root)
        return self.path_sum

    def get_path_num(self):
        digit_string = ""
        for val in self.path:
            digit_string += str(val)

        return int(digit_string)
    
    def search(self, node):
        self.path.append(node.val)

        has_left = node.left is not None
        has_right = node.right is not None

        if has_left and has_right:
            self.search(node.left)
            self.search(node.right)
        elif has_left:
            self.search(node.left)
        elif has_right:
            self.search(node.right)
        else:
            self.path_sum += self.get_path_num()
        
        self.path.pop()









        
