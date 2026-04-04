class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            M = int((L + R)/2)
            if (matrix[M][0] < target) and (matrix[M][-1] < target):
                L = M + 1
            elif (matrix[M][0] > target) and (matrix[M][-1] > target):
                R = M - 1
            elif target in matrix[M]:
                return True
            else:
                return False
        return False