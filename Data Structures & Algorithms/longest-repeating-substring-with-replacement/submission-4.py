class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        hash_map[s[0]] = 1
        l, r = 0, 0
        res = 0
        while r < len(s):
            max_val = 0
            for value in hash_map.values():
                max_val = max(max_val, value)
            
            if (r - l + 1) - max_val <= k:
                res = max(res, r - l + 1)
                r += 1
                if r < len(s):
                    hash_map[s[r]] = hash_map.get(s[r], 0) + 1

            else:
                hash_map[s[l]] = hash_map[s[l]] - 1
                l += 1
        return res
                
