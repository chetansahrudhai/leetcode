class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int,) -> int:
        adj_list = [[] for _ in range(n)]
        for x, y in hierarchy:
            x -= 1
            y -= 1
            adj_list[x].append(y)

        def merge(A, B):
            C = [-inf] * len(A)
            for i, a in enumerate(A):
                for j in range(len(A) - i):
                    C[i + j] = max(C[i + j], a + B[j])
            return C

        def dfs(u, p):
            d0 = [0] * (budget + 1)
            d1 = [0] * (budget + 1)
            for i in adj_list[u]:
                if i != p:
                    p0, p1 = dfs(i, u)
                    d0, d1 = merge(d0, p0), merge(d1, p1)

            res0 = d0[:]
            res1 = d0[:]
            cost = present[u]
            for z in range(cost, budget + 1):
                res0[z] = max(res0[z], d1[z - cost] + future[u] - cost)
            cost >>= 1
            for z in range(cost, budget + 1):
                res1[z] = max(res1[z], d1[z - cost] + future[u] - cost)
            return res0, res1
        return max(dfs(0, -1)[0])