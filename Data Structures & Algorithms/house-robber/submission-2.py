class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        i = 0
        while i < len(nums):
            tmp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = tmp
            i += 1

        return rob2

            