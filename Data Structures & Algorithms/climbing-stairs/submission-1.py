class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(x: int) -> int:
            if x in memo:
                return memo[x]

            if x <= 2:
                return x

            memo[x] = dfs(x - 1) + dfs(x - 2)
            return memo[x]

        return dfs(n)