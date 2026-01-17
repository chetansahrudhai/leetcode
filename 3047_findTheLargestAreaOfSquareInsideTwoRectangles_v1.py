class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0
        BL = len(bottomLeft)
        for i in range(BL):
            for j in range(i + 1, BL):
                xMin = max(bottomLeft[i][0], bottomLeft[j][0])
                xMax = min(topRight[i][0], topRight[j][0])
                yMin = max(bottomLeft[i][1], bottomLeft[j][1])
                yMax = min(topRight[i][1], topRight[j][1])
                if xMin < xMax and yMin < yMax:
                    k = min(xMax - xMin, yMax - yMin)
                    res = max(res, k)
        return res * res