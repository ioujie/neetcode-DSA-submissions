class Solution:
    def reverseBits(self, n: int) -> int:
        chars = ["0"] * 32
        i = 0
        while n > 0:
            if n & 1 == 1:
                chars[i] = '1'
            else:
                chars[i] = '0'
            n = n // 2
            i += 1

        return int("".join(chars), 2)