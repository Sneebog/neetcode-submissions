# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        newhead = head
        while head:
           arr.append(head.val)
           head = head.next
        head = newhead
        l = 1
        r = len(arr) - 1
        flag = False
        while l <= r:
            if flag:
                head.next = ListNode(arr[l])
                l += 1
            else:
                head.next = ListNode(arr[r])
                r -= 1
            head = head.next
            flag = not(flag)
        #return dummy.next



            