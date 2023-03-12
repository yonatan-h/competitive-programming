class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return is_symetric(root.left, root.right)



def is_symetric(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    
    if node1.val != node2.val:
        return False
    
    return is_symetric(node1.left, node2.right) and is_symetric(node1.right, node2.left)
    

#15min
#1sub