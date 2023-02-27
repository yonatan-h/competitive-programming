class DNode:
    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.prev = None
    
    def add_next(self, d_node):
        self.next = d_node
        d_node.prev = self

class MyCircularDeque:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        
        self.head = DNode(-1)
        self.tail = DNode(-1)
        self.head.add_next(self.tail)
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DNode(value)
        after_head = self.head.next

        self.head.add_next(new_node)
        new_node.add_next(after_head)
        self.size += 1

        return True
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DNode(value)
        before_tail = self.tail.prev

        before_tail.add_next(new_node)
        new_node.add_next(self.tail)
        self.size += 1

        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        after_after_head = self.head.next.next
        self.head.add_next(after_after_head)
        
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        before_before_tail = self.tail.prev.prev
        before_before_tail.add_next(self.tail)
        
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        return self.head.next.val
        

    def getRear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return 0 == self.size

    def isFull(self) -> bool:
        return self.max_size == self.size
        


#40min
#2sub