class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row0 = [0] * m
        col0 = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row0[i] = 1
                    col0[j] = 1

        for i in range(m):
            if row0[i] == 1:
                for j in range(n):
                    matrix[i][j] = 0
            else:
                for j in range(n):
                    if col0[j] == 1:
                        matrix[i][j] = 0