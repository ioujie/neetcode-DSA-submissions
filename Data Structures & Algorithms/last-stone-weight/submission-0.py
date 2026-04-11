class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if y == x:
                continue
            else:
                y -= x
                heapq.heappush(stones, -1 * y)
        
        if len(stones) == 0:
            return 0
        else:
            return -1 * stones[0]