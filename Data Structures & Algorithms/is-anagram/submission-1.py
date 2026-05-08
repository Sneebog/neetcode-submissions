class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashmap = {}
        t_hashmap = {}
        for i in range(0, len(s)):
            if s_hashmap.get(s[i]) is None: 
                s_hashmap[s[i]] = 1
            else:
                s_hashmap[s[i]] += 1

            if t_hashmap.get(t[i]) is None:
                t_hashmap[t[i]] = 1
            else:
                t_hashmap[t[i]] += 1
        
        if s_hashmap == t_hashmap:
            return True
        else:
            return False