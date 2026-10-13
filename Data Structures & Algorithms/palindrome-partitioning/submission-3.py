class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        # need to dfs through all the possible options
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
            return 
        
        dfs(0)
        return res



    def isPalin(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1 
            j -= 1
        return True
