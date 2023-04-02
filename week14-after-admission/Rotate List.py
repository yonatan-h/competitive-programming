# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        flag_length = k% get_length(head)
        if flag_length == 0: return head

        flag_head, flag_tail = get_flag(head, flag_length)

        flag_tail.next = head
        return flag_head

def get_length(first_node):
    cur = first_node
    length = 0
    while cur:
        length += 1
        cur = cur.next

    return length


def get_flag(first_node, flag_length):
    slow = first_node
    fast = first_node

    for i in range(flag_length): fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    flag_head = slow.next
    slow.next = None

    flag_tail  = fast

    return (flag_head, flag_tail)

