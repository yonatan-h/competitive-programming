# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_vals = defaultdict(list)
        self.save_index(root, 0)

        result = []

        levels = sorted(list(self.level_vals.keys()))
        for level in levels:
            result.append(self.level_vals[level])
            
        return result



    def save_index(self, node, level):
        if node is None:
            return
        
        self.level_vals[level].append(node.val)

        self.save_index(node.left, level+1)
        self.save_index(node.right, level+1)

#1sub