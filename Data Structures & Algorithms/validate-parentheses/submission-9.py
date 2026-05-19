class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        char_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        
        for c in s:
            if c in char_map:
                stack.append(char_map[c])  # push expected closing
            else:
                if not stack or stack.pop() != c:
                    return False

    
        return True if not stack else False