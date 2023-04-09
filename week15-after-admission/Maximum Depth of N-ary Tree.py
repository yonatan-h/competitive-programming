"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_level = 0
        self.dive(root, 1)
        return self.max_level
    
    def dive(self, node, level):
        if node is None:
            return
        self.max_level = max(self.max_level, level)

        for child in node.children:
            self.dive(child, level+1)
        
