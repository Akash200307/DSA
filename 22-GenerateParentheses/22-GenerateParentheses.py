# Last updated: 2/3/2026, 9:43:53 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,sol=[],[]
        def dfs(open_b,close_b):
            if len(sol)==2*n:
                res.append("".join(sol.copy()))
                return
            
            if open_b<n:
                sol.append("(")
                dfs(open_b+1,close_b)
                sol.pop()

            if close_b<open_b:
                sol.append(")")
                dfs(open_b,close_b+1)
                sol.pop()

        dfs(0,0)
        return res