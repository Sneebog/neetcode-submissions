class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_hashmap = {}
        #t_hashmap for letters
        for c in t:
            t_hashmap[c]= t_hashmap.get(c, 0) + 1
        s_hashmap = {}
        ex_s_hashmap = {}
        l = 0 
        count = 0
        length = len(s) + 1
        word = (0,0)
        #loop through r (sliding window)
        for r in range(0, len(s)):
            #if the letter is in the hashmap add it to the checking hashmap 
            # and that there isn't alreadt enough of the value
            #if the letter is in the hashmap add it to the checking hashmap 
            if s[r] in t_hashmap and t_hashmap.get(s[r], 0) > s_hashmap.get(s[r], 0):
                s_hashmap[s[r]] = s_hashmap.get(s[r], 0) + 1
            else:
                ex_s_hashmap[s[r]] = ex_s_hashmap.get(s[r], 0) + 1
                count += 1
            
            while s_hashmap == t_hashmap:
                if count + len(t) < length:
                    word = (l,r + 1)
                    length = count + len(t)

                if s[l] in ex_s_hashmap and ex_s_hashmap.get(s[l], 0) != 0:
                    ex_s_hashmap[s[l]] = ex_s_hashmap[s[l]]  - 1
                    count -= 1
                else:
                    s_hashmap[s[l]] = s_hashmap[s[l]] - 1
                l += 1

        return s[word[0]:word[1]]

            

            
            
            


