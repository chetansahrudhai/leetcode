class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        size = len(grid[0])
        r = len(grid) - 1
        c = res = 0
        while r >= 0 and c < size:
            if grid[r][c] < 0:
                res += size - c
                r -= 1
            else:
                c += 1
        return res