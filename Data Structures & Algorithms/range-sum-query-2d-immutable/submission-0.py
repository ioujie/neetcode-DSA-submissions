class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = []
        self.n = len(matrix[0])
        total = 0
        for r in matrix:
            for e in r:
                total += e
                self.preSum.append(total)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
                preSumR = self.preSum[self.getIdx(row, col2)]
                if self.getIdx(row, col1) < 1 :
                    preSumL = 0
                else:
                    preSumL = self.preSum[self.getIdx(row, col1) - 1]
                total += preSumR - preSumL
        return total

    def getIdx(self, row, col):
        return row * self.n + col
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)