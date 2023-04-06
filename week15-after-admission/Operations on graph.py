from collections import defaultdict


class Graph: #bidirectional
    def __init__(self):
        self.dict = defaultdict(list)

    def insert_edge(self, node1, node2):
        self.dict[node1].append(node2)
        self.dict[node2].append(node1)
        
    def get_neighbors(self, node):
        return self.dict[node]

def main():
    num_nodes = input()
    num_test_cases = int(input())
    graph = Graph()

    for _ in range(num_test_cases):
        line = list(map(int, input().split()))
        if line[0] == 1:
            node1 = line[1]
            node2 = line[2]
            graph.insert_edge(node1, node2)
        else:
            node = line[1]
            print(*graph.get_neighbors(node))

main()