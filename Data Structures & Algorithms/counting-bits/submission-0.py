class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def countOne(n):
            ans = 0
            while n > 0:
                if n & 1 == 1:
                    ans += 1
                n = n // 2
            
            return ans
        
        for i in range(0, n + 1):
            ans.append(countOne(i))
        
        return ans
