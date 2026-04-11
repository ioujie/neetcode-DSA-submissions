class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = []
        total = 0
        n = len(nums)
        for num in nums:
            total += num
            preSum.append(total)

        for i in range(0, n):
            if i > 0:
                preSumL = preSum[i - 1]
            else:
                preSumL = 0

            if i == n - 1:
                sumR = 0
            else:
                sumR = preSum[n - 1] - preSum[i]

            if preSumL == sumR:
                return i

        return -1