class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        i = 0
        x = 32
        while n:
            if n & 1:
                res = i - x if i - x > res else res
                x = i
            i += 1
            n >>= 1
        return res