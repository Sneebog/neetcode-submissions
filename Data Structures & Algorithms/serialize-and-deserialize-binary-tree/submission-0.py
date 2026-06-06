# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
            #use breath first search
        res = []
        q = deque()
        curr = root
        q.append(curr)
        while q :
            lenq = len(q)
            for i in range(0, lenq):
                curr = q.popleft()
                if curr:
                    res.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    res.append(None)
        #has the array in bfs order
        #now turn into str
        res_str = "" + str(res[0])
        for i in range(1, len(res)):
            res_str += " " + str(res[i])
        return res_str
    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        bfs_arr = data.split(" ")
        q = deque()
        if bfs_arr[0] == "None":
            return None
        root = TreeNode(int(bfs_arr[0]))
        q.append(root)
        cnt = 1
        while q and cnt < len(bfs_arr):
            node = q.popleft()

            if bfs_arr[cnt] != "None":
                node.left = TreeNode(int(bfs_arr[cnt]))
                q.append(node.left)
            cnt += 1

            if cnt < len(bfs_arr) and bfs_arr[cnt] != "None":
                node.right = TreeNode(int(bfs_arr[cnt]))
                q.append(node.right)
            cnt += 1
        return root
