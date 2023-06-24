# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = to_adj_list(root)
        print(adj_list)
        visited = {target.val}
        que = deque([target.val])

        for i in range(k):
            level_len = len(que)
            for _ in range(level_len):
                node = que.popleft()
                for neighbor in adj_list[node]:
                    if neighbor in visited: continue
                    que.append(neighbor)
                    visited.add(neighbor)
        return list(que)




def to_adj_list(root):
    adj_list = defaultdict(list)

    def traverse(node):
        nonlocal adj_list
        for neighbor in [node.left, node.right]:
            if neighbor == None: continue
            adj_list[node.val].append(neighbor.val)
            adj_list[neighbor.val].append(node.val)
            traverse(neighbor)
    
    traverse(root)
    return adj_list