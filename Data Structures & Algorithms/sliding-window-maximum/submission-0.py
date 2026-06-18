class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        ans = []

        l = 0
        for r in range(n):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()
            
            if r - l + 1 == k:
                ans.append(nums[dq[0]])
                l += 1

        return ans