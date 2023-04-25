class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.king = kingName
        self.deads = set()
        

    def birth(self, parent: str, child: str) -> None:
        self.graph[parent].append(child)
        

    def death(self, name: str) -> None:
        self.deads.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        self.recurse(self.king, inheritance_order)
        return inheritance_order

    def recurse(self, person, inheritance_order):
        if person not in self.deads:
            inheritance_order.append(person)

        for child in self.graph[person]:
            self.recurse(child, inheritance_order)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()