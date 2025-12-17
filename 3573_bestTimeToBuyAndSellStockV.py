class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        p = len(prices)
        first = prices[0]
        dp = [[0, -first, first] for _ in range(k + 1)]
        for day in range(1, p):
            current = prices[day]
            for trx in range(k, 0, -1):
                profit = dp[trx - 1][0]
                dp[trx][0] = max(dp[trx][0], dp[trx][1] + current, dp[trx][2] - current)
                dp[trx][1] = max(dp[trx][1], profit - current)
                dp[trx][2] = max(dp[trx][2], profit + current)        
        return dp[k][0]