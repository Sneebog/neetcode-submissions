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
                stack.append(c)
            else:
                if len(stack) > 0:
                    brack = stack.pop()
                    if char_map[brack] != c:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False