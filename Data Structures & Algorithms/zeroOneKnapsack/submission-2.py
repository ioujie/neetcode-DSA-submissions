class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        memo = {}
        def dfs(i, cap):
            if i >= n:
                return 0

            if (i, cap) in memo:
                return memo[(i, cap)]

            if weight[i] <= cap:
                skip = dfs(i + 1, cap)
                take = profit[i] + dfs(i + 1, cap - weight[i])
                memo[(i, cap)] = max(skip, take)
                return memo[(i, cap)]

            memo[(i, cap)] = dfs(i + 1, cap)
            return memo[(i, cap)]
 
        return dfs(0, capacity)