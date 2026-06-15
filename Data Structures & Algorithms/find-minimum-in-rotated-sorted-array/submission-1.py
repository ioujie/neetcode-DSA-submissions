class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            m = (left + right) // 2
            if nums[m] < nums[right]:
                right = m
            else:
                left = m + 1

        return nums[right]