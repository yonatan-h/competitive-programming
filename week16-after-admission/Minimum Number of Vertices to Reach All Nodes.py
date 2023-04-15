class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        pointers = set()
        pointeds = set()
        for edge in edges:
            pointer, pointed = edge

            pointers.add(pointer)
            pointeds.add(pointed)
        
        return list(pointers - pointeds)
            

