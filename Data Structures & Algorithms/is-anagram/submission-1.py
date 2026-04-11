class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False

        cntS, cntT = {}, {}

        for i in range(n):
            cntS[s[i]]= 1 + cntS.get(s[i], 0)
            cntT[t[i]] = 1 + cntT.get(t[i], 0)

        return cntS == cntT