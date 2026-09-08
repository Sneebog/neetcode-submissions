class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first = strs[0]
        for i in range(0, len(first)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or first[i] != strs[j][i]:
                    return first[0:i]
        return first