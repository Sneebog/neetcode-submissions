# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        while True: 
            num, minnum_pos = 1001, -1

            for i in range(0, len(lists)):
                if lists[i] and (minnum_pos == -1 or lists[i].val < lists[minnum_pos].val):
                    minnum_pos = i

            if minnum_pos == -1:
                break

            head.next = ListNode(lists[minnum_pos].val)
            if lists[minnum_pos]:
                lists[minnum_pos] = lists[minnum_pos].next
            head = head.next

        return dummy.next