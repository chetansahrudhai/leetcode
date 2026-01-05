class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in matrix:
            for j in i:
                res += abs(j)
        if str(matrix).count('-') % 2 == 0:
            return res
        else:
            largestNegative = max(x for row in matrix for x in row if x < 0)
            try:
                smallestPositive = min(x for row in matrix for x in row if x >= 0)
            except:
                return res + 2*largestNegative
            diff = min(smallestPositive, abs(largestNegative))
            return res - 2*diff