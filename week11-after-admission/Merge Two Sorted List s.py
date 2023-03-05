# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None) and (list2 == None):
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        return merge(list1, list2)
        
def merge(list1, list2):
    #needs list1 and list2 != None
    first_node = None
    current_node = ListNode()

    while list1 and list2:

        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next

        current_node = current_node.next

        if not first_node:
            first_node = current_node


    
    if list1:
        current_node.next = list1
    elif list2:
        current_node.next = list2
    
    return first_node


#20min
#1sub


