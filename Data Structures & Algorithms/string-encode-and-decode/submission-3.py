class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1

            length = int(s[l:r])
            decoded.append(s[r + 1: r + 1 + length])

            l = r + 1 + length

        return decoded