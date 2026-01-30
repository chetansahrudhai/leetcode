class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        S = len(source)

        transform = {}
        for o, c, co in zip(original, changed, cost):
            transform[(o, c)] = min(transform.get((o, c), INF), co)

        strings = set(original) | set(changed)

        for s in strings:
            transform[(s, s)] = 0

        X = list(strings)
        for w in X:
            for u in X:
                if (u, w) not in transform:
                    continue
                for v in X:
                    if (w, v) not in transform:
                        continue
                    costSum = transform[(u, w)] + transform[(w, v)]
                    if (u, v) not in transform or costSum < transform[(u, v)]:
                        transform[(u, v)] = costSum
        
        check = sorted(set(len(s) for s in strings))

        dp = [INF] * (S + 1)
        dp[0] = 0
        
        for i in range(S):
            if dp[i] == INF:
                continue

            if i < S and source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for l in check:
                if i + l > S:
                    continue
                
                so = source[i:i + l]
                ta = target[i:i + l]

                if (so, ta) in transform:
                    dp[i + l] = min(dp[i + l], dp[i] + transform[(so, ta)])
        
        return -1 if dp[S] == INF else dp[S]