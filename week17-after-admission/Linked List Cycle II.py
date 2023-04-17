# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        starting = True
        slow = head
        fast = head

        while slow != fast or starting:
            starting = False
            if not (fast and fast.next):
                return None

            slow = slow.next
            fast = fast.next.next
        

        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow