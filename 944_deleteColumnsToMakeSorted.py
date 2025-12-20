class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        s, z = len(strs), len(strs[0])
        for i in range(z):
            for j in range(1,s):
                if strs[j][i] < strs[j-1][i]:
                    res += 1
                    break
        return res