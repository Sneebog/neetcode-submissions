class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = set()
        subset = []
        def palin(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def check(cnt):
            if cnt == len(s):
                # if len(subset) == len(s):
                res.add(tuple(subset))
                return
            
            for i in range(cnt, len(s)):
                    if palin(cnt, i):
                        subset.append(s[cnt:i+1])
                        check(i+ 1)
                        subset.pop()
        check(0)
        return [list(comb) for comb in res]
