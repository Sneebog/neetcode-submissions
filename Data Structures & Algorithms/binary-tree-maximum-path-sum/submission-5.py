# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = root.val

        def dfs(root):
            if not root:
                return 0
            
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            left_val = max(left_val, 0)
            right_val = max(right_val, 0)

            self.max_val = max(self.max_val, root.val + left_val + right_val)
            return root.val + max(left_val, right_val)
        dfs(root)
        return self.max_val