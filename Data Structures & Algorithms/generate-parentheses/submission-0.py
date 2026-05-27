class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, op, cl):
            if cl > op:
                return
            if len(cur) == 2 * n:
                res.append(cur)
                return
            
            if op < n:
                cur += '('
                dfs(cur, op + 1, cl)
                cur = cur[:-1]
            if cl < n:
                cur += ')'
                dfs(cur, op, cl + 1)
                cur = cur[:-1]
        dfs('', 0, 0)
        return res
                
