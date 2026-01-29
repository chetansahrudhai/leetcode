class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        res = 0
        D = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            D[i][i] = 0
        for O, C, X in zip(original, changed, cost):
            i = ord(O) - 97
            j = ord(C) - 97
            D[i][j] = min(D[i][j], X)
        for w in range(26):
            for u in range(26):
                if D[u][w] == INF:
                    continue
                for v in range(26):
                    if D[w][v] != INF:
                        D[u][v] = min(D[u][v], D[u][w] + D[w][v])
        for S, T in zip(source, target):
            i = ord(S) - 97
            j = ord(T) - 97
            if i == j:
                continue
            if D[i][j] == INF:
                return -1
            res += D[i][j]
        return res