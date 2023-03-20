# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        val_counts = defaultdict(int)
        traverse_count(root, val_counts)


        val_count_pairs = list(val_counts.items())
        
        max_count = -float("inf")

        for (val, count) in val_count_pairs:
            max_count = max(max_count, count)


        modes = []
        for (val, count) in val_count_pairs:
            if count == max_count:
                modes.append(val)
        return modes


def traverse_count(node, val_counts):
    if node is None:
        return
    val_counts[node.val] += 1
    
    traverse_count(node.left, val_counts)
    traverse_count(node.right, val_counts)

#1sub