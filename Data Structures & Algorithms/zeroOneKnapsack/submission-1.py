from functools import cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        @cache
        def dfs(i, cap):
            if i >= n:
                return 0

            if weight[i] <= cap:
                skip = dfs(i + 1, cap)
                take = profit[i] + dfs(i + 1, cap - weight[i])
                return max(skip, take)

            return dfs(i + 1, cap)
 
        return dfs(0, capacity)