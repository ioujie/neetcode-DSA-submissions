class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        dirc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirc:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols:
                        continue
                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1