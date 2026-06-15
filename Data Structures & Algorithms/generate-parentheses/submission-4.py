class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def paren(open_brac, closed_brac):
            if open_brac == n and open_brac == closed_brac:
                res.append("".join(stack))
                return
            
            #two options open bracket or close bracket
            if open_brac < n:
                stack.append("(")
                paren(open_brac + 1, closed_brac)
                stack.pop()
            if closed_brac < open_brac:
                stack.append(")")
                paren(open_brac, closed_brac + 1)
                stack.pop()
        paren(0,0)
        return res