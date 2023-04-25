# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.nums = deque(preorder)
        return self.build(-float("inf"), float("inf"))
    
    def build(self, min, max):
        if not (self.nums and min < self.nums[0] < max):
            return None

        num = self.nums.popleft()
        node = TreeNode(num)

        node.left = self.build(min, num)
        node.right = self.build(num, max)

        return node



        
        

            



        