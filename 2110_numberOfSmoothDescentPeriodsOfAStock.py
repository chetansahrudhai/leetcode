class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result, descent, previous = 0, 0, -1
        for i in prices:
            descent = (-((i+1) == previous) & descent) + 1
            result += descent
            previous = i
        return result