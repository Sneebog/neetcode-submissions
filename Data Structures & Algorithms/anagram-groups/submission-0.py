class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        inserted_flag = False 
        for i in range(0, len(strs)):
            inserted_flag = False 
            for j in range(0, len(anagrams)):
                if len(anagrams[j][0]) == len(strs[i]):
                    str_hasha = {}
                    str_hash = {}
                    for k in range(0, len(strs[i])):
                        str_hasha[anagrams[j][0][k]] = str_hasha.get(anagrams[j][0][k], 0) + 1
                        str_hash[strs[i][k]] = str_hash.get(strs[i][k], 0) + 1
                    if str_hasha == str_hash:
                        anagrams[j].append(strs[i])
                        inserted_flag = True
                        break
            if not inserted_flag:     
                anagrams.append([strs[i]])

        return anagrams



            