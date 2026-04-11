class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def movRight(nums, n):
            tmp = nums[n-1]
            for i in range(n):
                tmp, nums[i] = nums[i], tmp
                
        simK = k % n
        for i in range(simK):
            movRight(nums, n)