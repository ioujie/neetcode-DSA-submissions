class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False

        count = [0]*26
        for i in range(lenS):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for v in count:
            if v != 0:
                return False

        return True 