class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def paren(cnt, par):
            if cnt == n:
                res.add(par)
                return
            #either insert in the position or don't?
            for i in range(0, len(par)):
                new_par = par[:i] + "()" + par[i:]
                paren(cnt+ 1, new_par)
        paren(1, "()")
        return [paren for paren in res]

            