class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_list = get_adj_list(adjacentPairs)
        terminal = get_terminal(adj_list)

        array = [terminal]
        que = deque([terminal])
        visited = {terminal}
        while que:
            node = que.pop()
            for neighbor in adj_list[node]:
                if neighbor in visited: continue
                array.append(neighbor)
                que.append(neighbor)
                visited.add(neighbor)
        return array

            





def get_adj_list(edges):
    adj_list = defaultdict(list)
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    return adj_list

def get_terminal(adj_list):
    for node in adj_list.keys():
        if len(adj_list[node]) == 1:
            return node

