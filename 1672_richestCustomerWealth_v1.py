class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxW = 0
        for i in range(len(accounts)):
            result = sum(accounts[i])
            maxW = max(maxW, result)
        return maxW