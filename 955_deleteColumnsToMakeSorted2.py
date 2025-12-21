class Solution:
    def minDeletionSize(self, strs):
        s, z = len(strs), len(strs[0])
        sort = [False] * (s - 1)
        res = 0
        for c in range(z):
            unordered = False
            for i in range(s - 1):
                if not sort[i] and strs[i][c] > strs[i + 1][c]:
                    unordered = True
                    break
            if unordered:
                res += 1
                continue
            for i in range(s - 1):
                if not sort[i] and strs[i][c] < strs[i + 1][c]:
                    sort[i] = True
            if all(sort):
                break
        return res