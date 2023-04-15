class Solution:
    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        self.is_connected = is_connected
        num_provinces = 0
        self.visited = set()

        for city in range(len(is_connected)):
            if city not in self.visited:
                self.visit(city)
                num_provinces += 1
                
        return num_provinces
                

    def visit(self, city):
        self.visited.add(city)
        for neighbour in range(len(self.is_connected)):
            if self.is_connected[city][neighbour] != 1:
                continue
            if neighbour in self.visited:
                continue
            self.visit(neighbour)
            
        

