class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        X = []
        for i in range(one + 1):
            In = []
            for j in range(zero + 1):
                In.append([0] * 2)
            X.append(In)
        X[0][0][0] = X[0][0][1] = 1
        for a in range(one + 1):
            for b in range(zero + 1):
                for w in range(1, limit + 1):
                    if a - w >= 0:
                        X[a][b][1] = (X[a][b][1] + X[a - w][b][0]) % mod
                    if b - w >= 0:
                        X[a][b][0] = (X[a][b][0] + X[a][b - w][1]) % mod
        return (X[one][zero][0] + X[one][zero][1]) % mod