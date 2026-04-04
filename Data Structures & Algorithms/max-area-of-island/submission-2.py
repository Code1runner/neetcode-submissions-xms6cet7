class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxSize = 0
        visited = set()
        def dfs(r,c):

            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr,c + dc)
            return size
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = dfs(r,c)
                    maxSize = max(size, maxSize)

        return maxSize
