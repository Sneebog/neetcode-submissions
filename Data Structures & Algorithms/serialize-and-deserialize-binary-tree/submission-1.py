# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        bfs = []
        q = deque()
        q.append(root)
        while q:
            lenq = len(q)
            for i in range(0, lenq):
                node = q.popleft()
                if node:
                    bfs.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    bfs.append(node)
        bfs_str = "" + str(bfs[0])
        for i in range(1, len(bfs)):
            bfs_str += " " + str(bfs[i])
        print(bfs_str)
        return bfs_str


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(" ")
        if arr[0] == "None":
            return None
        dummy = TreeNode(0)
        root = TreeNode(arr[0])
        dummy.right = root
        i = 1
        q = deque()
        q.append(root)
        while i < len(arr):
            node = q.popleft()

            if arr[i] != "None":
                node.left = TreeNode(arr[i])
                q.append(node.left)
            
            i += 1

            if i < len(arr) and arr[i]!= "None":
                node.right = TreeNode(arr[i])
                q.append(node.right)
            
            i += 1
        return dummy.right
            
        
