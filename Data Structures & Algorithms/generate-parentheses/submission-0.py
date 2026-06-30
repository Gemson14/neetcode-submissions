class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(open, close, pattern):
            if open == n and close == open:
                res.append(pattern)
                return
            
            if open == n and close < open:
                dfs(open, close + 1, pattern + ")")
                return

            if open == close:
                dfs(open + 1, close, pattern + "(")
                return

            dfs(open + 1, close, pattern + "(")
            dfs(open, close + 1, pattern + ")")
            return
            
        dfs(0,0,"")

        return res


                


        