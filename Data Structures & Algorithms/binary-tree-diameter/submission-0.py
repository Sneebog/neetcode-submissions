# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], diameter=None) -> int:
        if diameter is None:
            diameter = 0
        if not root:
            return diameter
    
        
        left = self.get_max(root.left)
        right = self.get_max(root.right)
        if left + right > diameter:
            diameter = left + right
        
        if left > right:
            return self.diameterOfBinaryTree(root.left, diameter)
        else:
            return self.diameterOfBinaryTree(root.right, diameter)    
      

    def get_max(self, root):
        if not root:
            return 0
        return max(self.get_max(root.left), self.get_max(root.right)) + 1