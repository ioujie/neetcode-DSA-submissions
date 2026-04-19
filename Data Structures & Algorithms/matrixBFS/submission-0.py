class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])

        if grid[0][0] == 1 or grid[Rows - 1][Cols - 1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        length = 0
        dirct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == Rows - 1 and c == Cols - 1:
                    return length

                for dr, dc in dirct:
                    if r + dr < 0 or c + dc < 0 or r + dr >= Rows or c + dc >= Cols or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited:
                        continue
                        
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            length += 1

        return -1

            