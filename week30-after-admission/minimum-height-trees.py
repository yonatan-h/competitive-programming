class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = get_adj_list(edges)
        in_degrees = get_in_degrees(edges)
        leaves = get_leaves(n, adj_list)

        for leaf in leaves:
            in_degrees[leaf] = 0

        que = deque(leaves)
        copy_que = []
        while que:
            copy_que = []
            for _ in range(len(que)):
                node = que.popleft()
                copy_que.append(node)

                for neighbor in adj_list[node]:
                    in_degrees[neighbor] -= 1

                    if in_degrees[neighbor] == 1:
                        que.append(neighbor)

        return copy_que
   

def get_in_degrees(edges):
    in_degrees = defaultdict(int)
    for node1, node2 in edges:
        in_degrees[node1] += 1
        in_degrees[node2] += 1
    return in_degrees

def get_adj_list(edges):
    adj_list = defaultdict(list)
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    return adj_list


def get_leaves(num_nodes, adj_list):
    leaves = []
    for node in range(num_nodes):
        if len(adj_list[node]) <= 1:
            leaves.append(node)
    return leaves
