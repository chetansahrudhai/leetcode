class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            res += sum(map(lambda x : x < 0, i))
        return res