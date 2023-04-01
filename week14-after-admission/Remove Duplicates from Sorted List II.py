# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, first_node: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(None)

        prev_node = head
        cur_node = first_node
        prev_node.next = cur_node


        #leave the tail node alone
        while cur_node and cur_node.next :
            if cur_node.val == cur_node.next.val:

                df_node = cur_node.next
                #pops until different val or None
                while df_node and df_node.val == cur_node.val:
                    df_node = df_node.next
                
                prev_node.next = df_node
                cur_node = df_node
                
            else:
                prev_node = cur_node
                cur_node = cur_node.next

        return head.next