class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        minutes, fresh = 0, 0
        queue = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))


        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr  < 0) or (nr >= ROWS) or (nc < 0) or (nc>= COLS) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1