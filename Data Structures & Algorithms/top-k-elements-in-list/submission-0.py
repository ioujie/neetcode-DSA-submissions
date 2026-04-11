class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans =[]
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for i in range(k):
            maxFreq = 0
            res = 0
            for key in d:
                if d[key] > maxFreq:
                    maxFreq = d[key]
                    res = key
            ans.append(res)
            del d[res]

        return ans