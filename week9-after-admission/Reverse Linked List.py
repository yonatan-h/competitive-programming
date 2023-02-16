# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:return head
        return get_new_head(head)

        
new_head = None

def get_new_head(head):
    flip_arrow(head)
    return new_head

def flip_arrow(node):
    
    if node.next == None:
        global new_head
        new_head = node
        return node
    
    next_node = flip_arrow(node.next)
    next_node.next = node
    node.next = None
    return node
    
#15min
#3sub
    