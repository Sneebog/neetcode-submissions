# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #visited every node
        if not preorder or not inorder:
            return None
        
        #root node
        node = TreeNode(preorder[0])
        #get the index of the root of in order
        mid = inorder.index(preorder[0])
        #left of Node
        # Has the rest of preorder and the left of mid in inorder
        node.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        #Right of Node
        #has from the next noder after i think and right of 
        node.right = self.buildTree(preorder[mid +1 :], inorder[mid + 1:])

        return node