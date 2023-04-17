# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, first_node: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = ListNode()

        node = first_node
        while node:
            inserted = node
            node = node.next
            insert(sorted_head, inserted)
        return sorted_head.next
        

def insert(sorted_head, inserted):
    node = sorted_head
    while node and node.next:
        if node.next.val > inserted.val:
            break
        node = node.next 
    
    old_next = node.next
    node.next = inserted
    inserted.next = old_next