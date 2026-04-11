class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = []
        total = 0
        for n in nums:
            total += n
            self.preSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preSumR = self.preSum[right]
        if left > 0:
            preSumL = self.preSum[left - 1]
        else:
            preSumL = 0
        return preSumR - preSumL


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)