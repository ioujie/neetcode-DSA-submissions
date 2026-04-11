class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []
        for idx, p in enumerate(points):
            dis = p[0]**2 + p[1]**2
            heap.append((dis, idx, p))

        heapq.heapify(heap)

        for i in range(k):
            ans.append(heapq.heappop(heap)[2])

        return ans

        



        
