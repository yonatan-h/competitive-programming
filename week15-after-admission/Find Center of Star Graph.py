class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = set()
        common.update(edges[0])

        for edge in edges:
            edge_set = set()
            edge_set.update(edge)
            common = common.intersection(edge_set)
        
        return list(common)[0]