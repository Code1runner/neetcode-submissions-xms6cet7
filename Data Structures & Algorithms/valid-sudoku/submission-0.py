class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sb = defaultdict(set)
        for r in range(9):
            for c in range(9):
                box_row = r // 3
                box_col = c // 3

                if board[r][c].isdigit():
                    num = board[r][c]
                    row_key = ('r', r)
                    col_key = ('c', c)
                    box_key = ('b', box_row, box_col)
                    if num not in sb[row_key] and num not in sb[col_key] and num not in sb[box_key]:
                        sb[row_key].add(num)
                        sb[col_key].add(num)
                        sb[box_key].add(num)
                    else:
                        return False
                else:
                    continue
        return True