# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        while head and head.next:
            if head.val in seen:
                return True
            else:
                seen.add(head.val)
            head = head.next
        return False