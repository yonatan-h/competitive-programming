class MyHashMap:

    def __init__(self):
        self.map = Map()
        

    def put(self, key: int, value: int) -> None:
        self.map.add(key, value)

    def get(self, key: int) -> int:
        return self.map.get_value(key)

    def remove(self, key: int) -> None:
        return self.map.remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class Node:
    def __init__(self,key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class Map:
    def __init__(self):
        self.arr = [Node() for _ in range(10000)]
        
    def hash(self, key):
        return key % len(self.arr)

    def add(self, key: int, val) -> None:
        if self.contains(key):
            node =self.get_node(key)
            node.val = val
            return
        
        head = self.arr[self.hash(key)]
        new_node = Node(key, val)
        old_next = head.next

        head.next = new_node
        new_node.next = old_next

    def remove(self, key: int) -> None:
        if not self.contains(key): return
        prev = self.get_prev_node(key)
        prev.next = prev.next.next

    def get_prev_node(self, key):
        index = self.hash(key)

        node = self.arr[index]

        while node.next and node.next.key != key:
            node = node.next
        return node
        
    
    def get_node(self, key):
        index = self.hash(key)
        node = self.arr[index]
        while node and node.key != key:
            node = node.next

        return node
    
    def get_value(self, key):
        node = self.get_node(key)
        if node: return node.val
        else: return -1

    def contains(self, key: int) -> bool:
        if self.get_node(key): return True
        else: return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)