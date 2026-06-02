# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        while True: 
            minnum, minnum_pos = 1001, -1

            for i in range(0, len(lists)):
                if lists[i] and lists[i].val < minnum:
                    minnum = lists[i].val
                    minnum_pos = i

            if minnum == 1001:
                break

            head.next = ListNode(minnum)
            if lists[minnum_pos]:
                lists[minnum_pos] = lists[minnum_pos].next
            head = head.next

        return dummy.next