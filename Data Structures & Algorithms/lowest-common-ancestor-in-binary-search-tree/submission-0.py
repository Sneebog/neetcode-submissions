# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = root
        def dfs(root, low, high):
            if not root:
                return 0
            self.ancestor = root
            if low.val > root.val:
                return dfs(root.right, low, high)
            elif root.val > high.val:
                return dfs(root.left, low, high)
            else:
                self.ancestor = root
                return 0
        
        if p.val < q.val:
            dfs(root, p, q)
        else:
            dfs(root, q, p)
        return self.ancestor
