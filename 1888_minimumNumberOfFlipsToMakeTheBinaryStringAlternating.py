class Solution:
    def minFlips(self, s: str) -> int:
        res = n = len(s)
        X = [0, 0]
        for i in range(n):
            X[(ord(s[i]) ^ i) & 1] += 1
        for i in range(n):
            j = ord(s[i])
            X[(j ^ i) & 1] -= 1
            X[(j ^ (n + i)) & 1] += 1
            res = min(res, min(X))
        return res