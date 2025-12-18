class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        p = len(prices)
        h = k//2
        sums = list(accumulate((strategy[x]*prices[x] for x in range(p)), initial=0))
        change = sum(prices[h:k])
        profit = max(sums[p], change+sums[p]-sums[k])
        for i in range(1, p+1-k):
            change += prices[i+k-1] - prices[i+h-1]
            profit = max(profit, change + sums[p] - sums[i+k] + sums[i])
        return profit