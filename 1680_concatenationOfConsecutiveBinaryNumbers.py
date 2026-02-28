class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        res = x = 0
        for i in range(1,n+1):
            if (i & (i-1)) == 0:
                x += 1
            res = ((res << x) | i) % mod
        return res