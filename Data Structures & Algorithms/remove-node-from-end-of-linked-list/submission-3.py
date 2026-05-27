# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        node = head
        count = 0
        #count how long the list 
        while node:
            node = node.next
            count +=1
        #calculate point to remove
        pos = count - n 
        node = head
        if pos == 0:
            return head.next
        
        while pos > 1:
            node = node.next
            pos -= 1
        
        node.next = node.next.next
        return head
        
        
