class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappop(nums)

        return nums[0]