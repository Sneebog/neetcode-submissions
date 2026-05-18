class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        print(k)
        s1_map = {}
        #loop to get s1 hash_map
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        print(s1_map)
        #Sliding window
        #Slides based on the length, removing / adding values as it goes along
        s2_map = {}
        l = 0
        for r in range(0, len(s2)):
            if (r - l + 1) > k:
                s2_map[s2[l]] = s2_map[s2[l]] - 1
                if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l])
                l += 1

            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            print(s2_map)
            if s2_map == s1_map:
                return True

        return False

