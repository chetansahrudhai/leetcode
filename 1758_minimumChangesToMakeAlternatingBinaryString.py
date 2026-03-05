class Solution:
    def minOperations(self, s: str) -> int:
        n, x = len(s), 0
        for i in range(n):
            x += (ord(s[i])^i)&1
        return min(x, n-x)