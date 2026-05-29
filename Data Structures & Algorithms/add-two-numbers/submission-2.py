# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l3 = ListNode()
        carry = 0
        while l1 or l2 or carry:
            # l1_val = l1.val if l1.val is not None else 0
            # l2_val = l2.val if l2.val is not None else 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            l3_val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            l3.next = ListNode(l3_val)
            l3 = l3.next
        
        return dummy.next
