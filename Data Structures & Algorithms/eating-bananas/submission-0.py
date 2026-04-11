class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            t = self.eatingTime(piles, mid, h)
            if t <= h:
                right = mid - 1
            else:
                left = mid + 1
            
        return left

    def eatingTime(self, piles: List[int], k: int, h: int) -> int:
        t = 0
        for p in piles:
            t += (p + k - 1) // k
            if t > h:
                return t
        return t  