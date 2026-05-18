class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        max_val = 0
        for r in range(0, len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_val = max(max_val, count[s[r]])
            while (r-l +1) - max_val > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(res, r- l + 1)
        return res
