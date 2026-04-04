class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1]== 1:
            return -1
        directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,1], [-1,-1], [1,-1]]
        visited = set()
        visited.add((0,0))
        queue = collections.deque([(0,0,1)])

        if not grid:
            return 0

        while len(queue) > 0:
            r,c,length = queue.popleft()
            if r == ROWS-1 and c == COLS-1:
                return length
            for dr, dc in directions:
                if min(r+dr,c+dc) < 0 or r+dr>=ROWS or c+dc>=COLS or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == 1:
                    continue
                visited.add((r+dr, c+dc))
                queue.append((r+dr, c+dc, length+1))
        return -1