# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            rightside = None
            lenq = len(q)
            for i in range(0, lenq):
                node = q.popleft()
                if node:
                    rightside = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside)
        return res
