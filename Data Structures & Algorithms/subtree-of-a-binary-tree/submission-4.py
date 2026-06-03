# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        def dfs(root, subRoot):
            if not root or self.flag:
                return None
            
            if root.val == subRoot.val:
                temp_root = root
                temp_subroot = subRoot
                self.flag = matching(temp_root, temp_subroot)

            if self.flag:
                return None

            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)
            return None
        
        def matching(q, p):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return matching(p.left, q.left) and matching(p.right, q.right)
            else:
                return False

        dfs(root, subRoot)
        return self.flag