# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_map = {}
        while head and head.next:
            if head.val in node_map:
                return True
            else:
                node_map[head.val] = head.next
            head = head.next
        return False