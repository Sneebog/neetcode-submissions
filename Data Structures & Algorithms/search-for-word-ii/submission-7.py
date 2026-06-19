class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
        #create trie then dfs through table using trie to check and breaking when not part
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word
        #Trie created now Dfs
        res = set()
        path = set()    
        ROWS, COLS = len(board), len(board[0])

        def dfs(curr, pos):
            r, c = pos[0], pos[1]
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in path or board[r][c] not in curr.children:
                return 
            char = board[r][c]
            path.add((r,c))
            curr = curr.children[char]
            if curr.word:
                res.add(curr.word)
            dfs(curr, (r + 1,c))
            dfs(curr, (r - 1,c))
            dfs(curr, (r,c + 1))
            dfs(curr, (r,c - 1))
            path.remove((r,c))
            return 
        
        for r in range(0, ROWS):
            for c in range(0, COLS):
                dfs(root, (r,c))
        return [word for word in res]