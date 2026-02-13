class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        idx = {}
        X = [[0, 0, 0]]
        for char in s:
            X.append(X[-1][:])
            X[-1]["abc".index(char)] += 1
        for i, (a, b, c) in enumerate(X):
            for key in [("abc", a - b, a - c),
                ("ab", a - b, c), ("bc", b - c, a), ("ca", c - a, b),
                ("a", b, c), ("b", c, a), ("c", a, b),
                ]:
                res = max(res, i - idx.get(key, i))
                idx.setdefault(key, i)
        return res