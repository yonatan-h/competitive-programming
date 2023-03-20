# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return sort_list(head)


def sort_list(head):
    if head is None or head.next is None:
        return head

    list1 = head
    list2 = break_half(head)

    print(list1.val, list2.val)

    sorted1 = sort_list(list1)
    sorted2 = sort_list(list2)
    return merge(sorted1, sorted2)


def break_half(head): #>= 2 elements. so prev_slow always a node
    prev_slow = None
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        prev_slow = slow
        slow = slow.next

    prev_slow.next = None
    return slow

def merge(head1, head2):
    new_head = ListNode()
    cur_node = new_head

    while head1 and head2:
        appended = None
        if head1.val < head2.val:
            cur_node.next = head1
            head1 = head1.next
        else:
            cur_node.next = head2
            head2 = head2.next

        cur_node = cur_node.next #append
        cur_node.next = None #for safety
    
    if head1:
        cur_node.next = head1
    elif head2:
        cur_node.next = head2
    
    return new_head.next
    


#1sub