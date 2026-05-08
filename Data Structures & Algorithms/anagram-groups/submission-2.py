class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            str_hash = {}
            for i in range(0, len(word)):
                str_hash[word[i]] = str_hash.get(word[i], 0) + 1
            
            
            anagram_val = tuple(sorted(str_hash.items()))
            if anagram_val not in anagrams:
                anagrams[anagram_val] = []
            anagrams[anagram_val].append(word)
        
        return list(anagrams.values())