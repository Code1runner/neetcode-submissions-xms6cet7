class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ROWS, COLS = m, n
        grid = [[0]*COLS for i in range(ROWS)]

        def memoization(m, n):

            if m == ROWS or n == COLS:
                return 0

            if m == ROWS -1 or n == COLS - 1:
                return 1
            
            if grid[m][n] > 0:
                return grid[m][n]
            
            grid[m][n] = memoization(m+1, n) + memoization(m, n+1)
            return grid[m][n]

        return memoization(0,0)
            

            
