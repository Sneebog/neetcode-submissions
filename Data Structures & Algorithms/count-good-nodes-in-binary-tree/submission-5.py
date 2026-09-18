# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_node):
            #base case 
            if not node:
                return 0
            
            if node.val < max_node:
                return dfs(node.left, max_node) + dfs(node.right, max_node)
            else:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
        return dfs(root, root.val)
