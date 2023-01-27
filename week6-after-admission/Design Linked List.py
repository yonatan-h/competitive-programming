class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def set_next(self, node):
        self.next = node
        
    def get_next(self):
        return self.next
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        current_node = self.head
        for _ in range(index+1):
            current_node = current_node.get_next()

        return current_node.val
        
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0)

        
    
    def print(self):
        current_node = self.head
        
        while current_node:
            current_node = current_node.get_next()
            print(current_node.val, end = ", ")
        print()
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.length == 0:
            self.head.set_next(new_node)
            self.tail.set_next(new_node)
        else:
            old_last_node = self.tail.get_next()
            old_last_node.set_next(new_node)
            self.tail.set_next(new_node)

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= self.length: return
        
        new_node = Node(val)

        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.get_next()
            
        next_node = prev_node.get_next()
        new_node.set_next(next_node)
        prev_node.set_next(new_node)


        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length: return
        
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.get_next()
            
        cur_node = prev_node.get_next()
        next_node = cur_node.get_next()

        prev_node.set_next(next_node)

        

        
        


#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(1)
print(param_1)
# obj.addAtHead(99)
# obj.addAtTail(88)
# obj.addAtIndex(1,5)
# obj.deleteAtIndex(1)