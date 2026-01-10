class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = [0] * (l2 + 1)
        for x in range(1, l2 + 1):
            dp[x] = dp[x - 1] + ord(s2[x - 1])
        for i in range(1, l1 + 1):
            z = dp[0]
            dp[0] += ord(s1[i - 1])
            for j in range(1, l2 + 1):
                buffer = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = z
                else:
                    dp[j] = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
                z = buffer
        return dp[l2]