# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #slow , fast = head, head
        if not head.next:
            return None
        node = head
        count = 0
        #count how long the list is using fast
        while node:
            node = node.next
            count +=1
        # #if odd length 
        # if fast:
        #     count += 1
        #slow should be halfway
        #calculate point to remove
        pos = count - n 
        print(pos)
        node = head
        if pos == 0:
            return head.next
        else:
            while pos > 1:
                node = node.next
                pos -= 1
        
            node.next = node.next.next
            return head
        
        
