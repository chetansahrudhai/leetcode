class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        z = len(strs[0])
        dp = [1] * z
        for i in range(z):
            for j in range(i):
                if all(x[j] <= x[i] for x in strs):
                    dp[i] = max(dp[i], dp[j] + 1)
        return (z - max(dp))