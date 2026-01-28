class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        inf = float('inf')
        g, z = len(grid), len(grid[0])
        dp = [[inf] * z for _ in range(g)]
        dp[0][0] = 0
        L = defaultdict(list)
        for i in range(g):
            for j in range(z):
                L[grid[i][j]].append((i, j))
        
        def update():
            for i in range(g):
                for j in range(z):
                    temp = grid[i][j] + min(dp[i-1][j] if i else inf, dp[i][j-1] if j else inf)
                    if temp < dp[i][j]:
                        dp[i][j] = temp
        
        update()
        keys = sorted(L, reverse=True)
        for _ in range(k):
            D = inf
            for key in keys:
                for i, j in L[key]:
                    if dp[i][j] < D: D = dp[i][j]
                for i, j in L[key]:
                    dp[i][j] = D
            update()
        return dp[-1][-1]