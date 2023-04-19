class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        

    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index+1):
            cur = cur.next
            if cur is None: return -1
        
        return cur.val
    

        
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

        if not self.tail.next:
            self.tail.next = node
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        
        if not self.tail.next:
            self.head.next = node
            self.tail.next = node
        else:
            self.tail.next.next = node
            self.tail.next = node
 
    def addAtIndex(self, index: int, val: int) -> None:
        prev = self.head
        for i in range(index):
            prev = prev.next
            if prev is None: return -1
        
        node = Node(val)

        forwarded = prev.next
        prev.next = node
        node.next = forwarded

        if self.tail.next == prev: #is last node
            self.tail.next = node


    def deleteAtIndex(self, index: int) -> None:
        prev = self.head
        for i in range(index):
            prev = prev.next
            if prev is None or prev.next is None:
                return -1
        
        cur = prev.next
        if cur.next:
            prev.next = cur.next
        else:
            prev.next = None
            self.tail.next = prev
        
