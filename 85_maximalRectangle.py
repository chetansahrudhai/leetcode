class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        z = len(matrix[0])
        dims = [0] * (z + 1)
        res = 0
        for row in matrix:
            for i in range(z):
                dims[i] = dims[i] + 1 if row[i] == "1" else 0
            S = [-1]
            for i in range(z + 1):
                while dims[i] < dims[S[-1]]:
                    L = dims[S.pop()]
                    B = i - S[-1] - 1
                    res = max(L*B, res)
                S.append(i)
        return res