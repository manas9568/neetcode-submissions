class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = 0
        closed = 0
        res = []
        def f(op,close,curr):
            if op == close and op == n:
                res.append(curr)
                curr = ""
            if op > close:
                f(op,close+1,curr+")")
            if op < n:
                f(op+1,close,curr+"(")
        f(0,0,"")
        return res


                

        