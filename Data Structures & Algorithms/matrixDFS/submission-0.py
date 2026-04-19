class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        def dfs(grid, r, c, visited):
            if r < 0 or c < 0 or r == Rows or c == Cols or (r, c) in visited or grid[r][c] == 1:
                return 0

            if r == Rows - 1 and c == Cols - 1:
                return 1

            visited.add((r, c))

            cnt = 0
            cnt += dfs(grid, r - 1, c, visited)
            cnt += dfs(grid, r + 1, c, visited)
            cnt += dfs(grid, r, c - 1, visited)
            cnt += dfs(grid, r, c + 1, visited)

            visited.remove((r, c))

            return cnt

        return dfs(grid, 0, 0, set())