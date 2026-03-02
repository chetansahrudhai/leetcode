class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeroes = []
        swaps = 0
        for row in grid:
            z = 0
            x = n - 1
            while x >= 0 and row[x] == 0:
                z += 1
                x -= 1
            zeroes.append(z)
        for i in range(n):
            count = n - 1 - i
            x = i
            while x < n and zeroes[x] < count:
                x += 1
            if x == n:
                return -1
            swaps += (x - i)
            while x > i:
                zeroes[x], zeroes[x - 1] = zeroes[x - 1], zeroes[x]
                x -= 1
        return swaps