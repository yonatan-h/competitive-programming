class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.path = [0]
        self.paths = []
        self.search(0)
        return self.paths
    
    def search(self, node):
        if node == len(self.graph)-1:
            self.paths.append(self.path[:])
            return


        for neighbour in self.graph[node]:
            self.path.append(neighbour)
            self.search(neighbour)
            self.path.pop()


            
