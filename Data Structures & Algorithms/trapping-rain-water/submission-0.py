class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        trapped = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                trapped += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                trapped += maxR - height[r]

        return trapped
            