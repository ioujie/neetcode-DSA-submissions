class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        up = -1
        down = m - 1

        left = 0
        right = n - 1

        while up <= down:
            mid = (up + down) // 2 
            if matrix[mid][0] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                return True
        
        row = down

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True

        return False