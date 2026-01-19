class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, z = len(mat), len(mat[0])
        P = [[0] * (z + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, z + 1):
                P[i][j] = (mat[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1])
        side = min(m, z)
        while side > 0:
            for i in range(m - side + 1):
                for j in range(z - side + 1):
                    x = (P[i+side][j+side] - P[i][j+side] - P[i+side][j] + P[i][j])
                    if x <= threshold:
                        return side
            side -= 1
        return 0