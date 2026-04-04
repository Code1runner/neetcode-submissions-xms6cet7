class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_r, zero_c = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_r.add(r)
                    zero_c.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in zero_r or c in zero_c:
                    matrix[r][c] = 0
                    

        