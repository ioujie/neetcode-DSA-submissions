class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[Rows - 1][Cols - 1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        length = 1
        dirct = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == Rows - 1 and c == Cols - 1:
                    return length

                for dr, dc in dirct:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= Rows or nc >= Cols or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))

            length += 1
        
        return -1

