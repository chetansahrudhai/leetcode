class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in prices:
            if sell < i - buy:
                sell = i - buy
            if i < buy:
                buy = i
        return sell