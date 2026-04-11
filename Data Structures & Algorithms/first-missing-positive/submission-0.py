class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums.sort()
        for n in nums:
            if n > 0:
                if ans == n:
                    ans += 1

        return ans