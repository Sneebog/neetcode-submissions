class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res, let = "", ""
        flag = True
        count = 0 
        while flag:
            res += let
            if count >= len(strs[0]):
                flag = False
            else:
                let = strs[0][count]
                for i in range(1, len(strs)):
                    if count >= len(strs[i]) or let != strs[i][count]:
                        flag = False
                        break
                count +=1 
        return res 
            

        