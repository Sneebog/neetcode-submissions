class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = set()
        #hash map
        digit_map = {
            2: ("a", "b", "c"),
            3: ("d", "e", "f"),
            4: ("g", "h", "i"),
            5: ("j", "k", "l"),
            6: ("m", "n", "o"),
            7: ("p", "q", "r", "s"),
            8: ("t", "u", "v"),
            9: ("w", "x", "y", "z"),
        }
        
        def add_digit(cnt,word):
            if cnt == len(digits):
                res.add(word)
                return 
            
            #go through every possible character
            num = int(digits[cnt])
            chars = digit_map[num]
            for i in range(0, len(chars)):
                tmp_word = word + chars[i]
                add_digit(cnt + 1, tmp_word)
        add_digit(0, "")
        return [word for word in res]

            
