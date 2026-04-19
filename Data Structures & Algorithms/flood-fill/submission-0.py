class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Rows = len(image)
        Cols = len(image[0])
        sp = image[sr][sc]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or image[r][c] == color or image[r][c] != sp:
                return

            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)

        return image
