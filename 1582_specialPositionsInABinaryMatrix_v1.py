class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(sum(c)==1==sum(mat[c.index(1)]) for c in zip(*mat))