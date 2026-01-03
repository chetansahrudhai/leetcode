class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        same = 6  # c1-c2-c1 pattern
        diff = 6  # c1-c2-c3 pattern
        for _ in range(2, n + 1):
            i = (same * 3 + diff * 2) % mod
            j = (same * 2 + diff * 2) % mod
            same, diff = i, j
        return (same+diff)%mod