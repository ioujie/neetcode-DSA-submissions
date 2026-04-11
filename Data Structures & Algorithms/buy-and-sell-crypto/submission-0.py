class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for p in prices:
            maxProfit = max(p - minPrice, maxProfit)
            minPrice = min(p, minPrice)

        return maxProfit