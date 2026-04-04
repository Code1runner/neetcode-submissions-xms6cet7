class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ROWS = m
        COLS = n

        def dfs(m, n):

            if m == ROWS or n == COLS:
                return 0
            
            if m == ROWS -1 and n == COLS -1:
                return 1

            return dfs(m+1,n) + dfs(m,n+1)

        return dfs(0,0)