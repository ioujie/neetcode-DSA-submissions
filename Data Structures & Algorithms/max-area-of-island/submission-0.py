class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        Rows = len(grid)
        Cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1

            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)

            return area

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans