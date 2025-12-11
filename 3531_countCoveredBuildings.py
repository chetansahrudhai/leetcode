class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res = 0
        minCol = [n+1]*(n+1)
        maxCol = [0]*(n+1)
        minRow = [n+1]*(n+1)
        maxRow = [0]*(n+1)
        for i,j in buildings:
            minCol[i] = min(minCol[i], j)
            maxCol[i] = max(maxCol[i], j)
            minRow[j] = min(minRow[j], i)
            maxRow[j] = max(maxRow[j], i)
        for i, j in buildings:
            if minCol[i] < j < maxCol[i] and minRow[j] < i < maxRow[j]: res += 1
        return res