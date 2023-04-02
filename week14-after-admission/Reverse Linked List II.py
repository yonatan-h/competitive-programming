# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, first_node: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        return reverse_between(first_node, left, right)


def reverse_between(first_node, left, right):
    before_left, left_node, right_node, after_right = separate(first_node, left, right)
    reverse_list(left_node)

    if before_left is None:
        left_node.next = after_right
        return right_node
    else:
        before_left.next = right_node
        left_node.next = after_right
        return first_node


    


def separate(first_node, left, right):
    before_left = None
    left_node = None
    right_node = None
    after_right = None

    cur = first_node
    for i in range(1, right+1):
        next_node = cur.next

        if i == left:
            left_node = cur
            if before_left: before_left.next = None

        if i == right:
            right_node = cur
            after_right = right_node.next
            right_node.next = None

        if left_node is None:
            before_left = cur

        cur = next_node
    
    return (before_left, left_node, right_node, after_right)

def reverse_list(first_node):
    prev = None
    cur = first_node

    while cur:
        next_node = cur.next

        cur.next = prev #flip arrow

        prev = cur
        cur = next_node
    


    




