class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            str_hashmap = {}
            for char in word:
                str_hashmap[char] = str_hashmap.get(char, 0) + 1
            
            anagram = str(sorted(str_hashmap.items()))
            anagrams.setdefault(anagram, []).append(word)

        return list(anagrams.values()) 
        

