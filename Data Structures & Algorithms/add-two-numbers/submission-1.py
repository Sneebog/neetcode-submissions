# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #get the numbers by looping through each 
        l1_rev = l1_num = l2_rev = l2_num = ""
        while l1:
            l1_rev = l1_rev + str(l1.val)
            l1 = l1.next

        #L2 loop
        while l2:
            l2_rev = l2_rev + str(l2.val)
            l2 = l2.next

        # Add them
        for i in range(len(l1_rev) -1, -1 , -1):
            l1_num = l1_num + l1_rev[i]

         # Add them
        for i in range(len(l2_rev) -1, -1 , -1):
            l2_num = l2_num + l2_rev[i]

        #Output as Linked list
        l3_str = str(int(l1_num) + int(l2_num))
        dummy = l3 = ListNode()
        for i in range(len(l3_str) -1, -1 , -1):
            l3.next = ListNode(l3_str[i])
            l3 = l3.next

        return dummy.next

