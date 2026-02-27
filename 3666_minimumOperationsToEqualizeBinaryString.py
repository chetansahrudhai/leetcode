def ceil(x, y):
    return (x + y - 1) // y
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero = s.count("0")
        if n == k:
            return 0 if zero == 0 else 1 if zero == n else -1
        res = inf
        if zero % 2 == 0:
            M = max(ceil(zero, k), ceil(zero, n - k))
            M += M & 1
            res = min(res, M)
        if zero % 2 == k % 2:
            M = max(ceil(zero, k), ceil(n - zero, n - k))
            M += M & 1 == 0
            res = min(res, M)
        return res if res < inf else -1