class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[-1]*COLS for i in range(ROWS)] 

        def memoization(r, c):

            if r == ROWS or c == COLS:
                return 0
                
            if grid[r][c] > -1:
                return grid[r][c]

            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            grid[r][c] = memoization(r+1, c) + memoization(r, c+1)
            return grid[r][c]
        return memoization(0,0)
