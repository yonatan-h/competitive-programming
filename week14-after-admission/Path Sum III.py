# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.target = targetSum

        self.prefix = 0
        self.prefix_counts = defaultdict(int)
        self.prefix_counts[0] = 1

        self.traverse_count(root)
        return self.count

    def traverse_count(self, node):

        if not node:
            return

        #forward phase
        self.prefix += node.val
        self.prefix_counts[self.prefix] += 1

        self.traverse_count(node.left)
        self.traverse_count(node.right)

        self.count += self.prefix_counts[self.prefix - self.target]
        if self.prefix == self.prefix - self.target:
            self.count -= 1
        
        #back phase
        self.prefix_counts[self.prefix] -= 1
        self.prefix -= node.val

