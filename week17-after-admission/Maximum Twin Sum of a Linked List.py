# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first_half = head
        middle_node = get_middle_node(head)
        second_half = reverse(middle_node)

        first_node = first_half
        second_node = second_half
        max_twin_sum = 0
        
        while first_node and second_node:
            twin_sum = first_node.val + second_node.val
            max_twin_sum = max(max_twin_sum, twin_sum)

            first_node = first_node.next
            second_node = second_node.next
        return max_twin_sum

        

def get_middle_node(head):
    slow = head
    fast = head

    while fast:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    prev = None
    node = head

    while node:
        next = node.next
        node.next = prev

        prev = node
        node = next
    return prev
