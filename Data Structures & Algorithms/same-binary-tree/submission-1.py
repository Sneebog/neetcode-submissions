# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []
        def dfs(root, tree_arr):
            if not root:
                tree_arr.append(None)
                return 0
            tree_arr.append(root.val)
            left = dfs(root.left, tree_arr)
            right = dfs(root.right, tree_arr)

            return 1
        dfs(q, q_arr)
        dfs(p, p_arr)
        if p_arr == q_arr:
            return True
        else:
            return False

