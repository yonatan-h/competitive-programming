class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = build_graph(bombs)
        return get_max_chain(graph)


def build_graph(bombs):
    adj_list = defaultdict(list)
    for i in range(len(bombs)):
        for j in range(len(bombs)):
            if i == j: continue
            x1,y1,r1 = bombs[i]
            x2,y2,r2 = bombs[j]

            if (x1-x2)**2 + (y1-y2)**2 <= r1**2:
                adj_list[i].append(j)
    return adj_list

def get_max_chain(adj_list):
    max_chain = 1
    nodes = list(adj_list.keys())
    for node in nodes:
        node_set = set()
        count_under(node, adj_list, node_set)
        chain_size = len(node_set)
        max_chain = max(max_chain, chain_size)
        
    return max_chain

def count_under(node, adj_list, node_set):
    node_set.add(node)
    for child in adj_list[node]:
        if child  not in node_set:
            count_under(child, adj_list, node_set)
         
        
    



