class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = n

        return False