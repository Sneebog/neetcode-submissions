class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_sort = sorted(s)
        t_sort = sorted(t)

        for i in range (0, len(s)):
            if s_sort[i] != t_sort[i]:
                return False
        return True
