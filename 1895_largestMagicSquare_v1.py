class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res = 1
        g, z = len(grid), len(grid[0])

        def magic(a, b, c):
            s = None
            for x in range(a, a + c):
                row = sum(grid[x][b:b + c])
                if s is None: s = row
                elif s != row: return False
            for y in range(b, b + c):
                if sum(grid[x][y] for x in range(a, a + c)) != s:
                    return False
            if sum(grid[a + d][b + d] for d in range(c)) != s:
                return False
            if sum(grid[a + d][b + c - 1 - d] for d in range(c)) != s:
                return False
            return True
        
        for i in range(2, min(g, z) + 1):
            for j in range(g - i + 1):
                for k in range(z - i + 1):
                    if magic(j, k, i):
                        res = i
        return res