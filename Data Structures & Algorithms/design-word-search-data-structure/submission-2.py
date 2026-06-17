class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(cur, i):
            if i == len(word):
                if cur.endOfWord:
                    return True
                else:
                    return False
            #normal char
            #print(word[i], cur)
            if word[i] != ".":
                #print(word[i], cur)
                if word[i] not in cur.children:
                    return False
                return dfs(cur.children[word[i]], i+1)
            
            #any char 
            for c in cur.children:
                if dfs(cur.children[c], i + 1):
                    return True     
            return False 

        return dfs(cur, 0)