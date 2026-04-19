class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])

        if grid[0][0] == 1 or grid[Rows - 1][Cols - 1] == 1:
            return 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or grid[r][c] == 1:
                return 0

            if r == Rows - 1 and c == Cols - 1:
                return 1

            grid[r][c] = 1
            cnt = (
                dfs(r - 1, c) +
                dfs(r + 1, c) +
                dfs(r, c - 1) +
                dfs(r, c + 1)
            )
            grid[r][c] = 0

            return cnt

        return dfs(0, 0)