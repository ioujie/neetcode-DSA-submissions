class Solution:
    def decodeString(self, s: str) -> str:
        decoded = []
        count = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = 10*k + int(c)
            elif c == '[':
                decoded.append(cur)
                count.append(k)
                cur = ""
                k = 0
            elif c == ']':
                tmp = cur
                cur = decoded.pop()
                cnt = count.pop()
                cur += cnt*tmp
            else:
                cur += c

        return cur