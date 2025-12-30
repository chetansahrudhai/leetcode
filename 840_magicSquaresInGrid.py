class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        if row < 3 or col < 3:
            return 0
        for i in range(row - 2):
            for j in range(col - 2):
                fr = True
                nums = [False] * 10
                
                for x in range(3):
                    for y in range(3):
                        num = grid[i + x][j + y]
                        if num < 1 or num > 9 or nums[num]:
                            fr = False
                            break
                        nums[num] = True
                    if not fr:
                        break
                if not fr:
                    continue

                total = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                for x in range(3):
                    if grid[i+x][j] + grid[i+x][j+1] + grid[i+x][j+2] != total:
                        fr = False
                for y in range(3):
                    if grid[i][j+y] + grid[i+1][j+y] + grid[i+2][j+y] != total:
                        fr = False
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != total:
                    fr = False
                if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != total:
                    fr = False

                if fr:
                    res += 1
        return res