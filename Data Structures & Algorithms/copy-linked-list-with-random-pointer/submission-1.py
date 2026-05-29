"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy ={None: None}
        dummy = head
        while head:
            oldtoCopy[head] = Node(head.val)
            head = head.next
        head = dummy
        while head:
            oldtoCopy[head].next = oldtoCopy[head.next]
            oldtoCopy[head].random = oldtoCopy[head.random]
            head = head.next
        
        return oldtoCopy[dummy]
