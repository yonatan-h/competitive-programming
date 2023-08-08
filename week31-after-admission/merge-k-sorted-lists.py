# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val_nodes = defaultdict(list)
        heap = []
        for linked_list in lists:
            cur_node = linked_list
            while cur_node:
                top = cur_node
                cur_node = cur_node.next 
                top.next = None
                val_nodes[top.val].append(top)
                heap.append(top.val)
        heapify(heap)
        head = ListNode()
        cur = head
        
        for _ in range(len(heap)):
            val = heappop(heap)
            node = val_nodes[val].pop()
            cur.next = node
            cur = cur.next
        
        return head.next
            