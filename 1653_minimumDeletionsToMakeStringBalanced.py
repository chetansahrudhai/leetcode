class Solution:
    def minimumDeletions(self, s: str) -> int:
        x = res = 0
        for i in s:
            if i == 'b':
                x += 1
            elif x:
                res += 1
                x -= 1
        return res