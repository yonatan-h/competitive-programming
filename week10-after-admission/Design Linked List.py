class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
 
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0
        
    def addToHeadAndTail(self, val):
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.tail.next = new_node
        self.length += 1



    def removeFromHeadAndTail(self):
        self.head.next = None
        self.tail.next = None
        self.length -= 1


    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        
        return cur.val
        
        

    def addAtHead(self, val: int) -> None:
        if self.length == 0:
            self.addToHeadAndTail(val)
        else:
            new_node = Node(val)

            new_node.next = self.head.next
            self.head.next = new_node
            self.length += 1



        
    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addToHeadAndTail(val)
        elif index >= self.length:
            return -1
        elif index == self.length - 1:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            cur = self.head
            for _ in range(index):
                cur = cur.next

            new_node.next = cur.next
            cur.next = new_node
            self.length += 1



    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addToHeadAndTail(val)
        else:
            new_node = Node(val)
            old_last_node = self.tail.next
            old_last_node.next = new_node

            self.tail.next = new_node
            self.length += 1
        



        
    def deleteAtIndex(self, index: int) -> None:
        if self.length == 0:
            return -1
        elif self.length == 1:
            self.removeFromHeadAndTail()
        elif index >= self.length:
            return -1
        else:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            prev.next = prev.next.next

            if index == self.length - 1:
                self.tail.next = prev.next

            self.length -= 1


    def print(self):
        cur = self.head.next
        print("my length is", self.length)
        while cur != None:
            print(cur.val, end=", ")
            cur = cur.next
        print("---")


#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtTail(6)
obj.deleteAtIndex(0)
obj.print()


# obj.addAtHead(99)
# obj.addAtTail(88)
# obj.addAtIndex(1,5)
# obj.deleteAtIndex(1)