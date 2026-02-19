class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, temp, streak = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                streak += 1
            else:
                temp = streak
                streak = 1
            if streak <= temp:
                res += 1
        return res                 