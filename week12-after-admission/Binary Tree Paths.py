# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        cur_path = []

        def run_around(node):
            if node == None:
                return


            cur_path.append(str(node.val))
            if node.left or node.right:

                run_around(node.left)
                run_around(node.right)

            else:
                paths.append("->".join(cur_path))
            cur_path.pop()
            
        run_around(root)
        return paths
    
#1sub
#30min

